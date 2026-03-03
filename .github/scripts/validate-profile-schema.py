#!/usr/bin/env python3
"""Validate SpiritSafe profile linkage and metadata graph schema rules."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


def get_nested(data: dict[str, Any], dotted_path: str) -> Any:
    current: Any = data
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def validate_required_paths(
    data: dict[str, Any],
    required_paths: list[str],
    error_prefix: str,
    errors: list[str],
) -> None:
    for path in required_paths:
        value = get_nested(data, path)
        if value is None:
            errors.append(f"{error_prefix}: missing required key '{path}'")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    profiles_root = repo_root / "profiles"

    if not profiles_root.exists():
        print("No profiles directory found; skipping linkage schema validation")
        return 0

    errors: list[str] = []
    metadata_by_profile: dict[str, dict[str, Any]] = {}

    profile_dirs = sorted(
        p
        for p in profiles_root.iterdir()
        if p.is_dir() and (p / "profile.yaml").exists() and (p / "metadata.yaml").exists()
    )

    for profile_dir in profile_dirs:
        profile_name = profile_dir.name
        profile_data = load_yaml(profile_dir / "profile.yaml")
        metadata_data = load_yaml(profile_dir / "metadata.yaml")
        metadata_by_profile[profile_name] = metadata_data

        statements = profile_data.get("statements", [])
        statement_ids = {
            st.get("id")
            for st in statements
            if isinstance(st, dict) and st.get("id")
        }

        # Validate statement-level linkage whenever entity_profile is present
        for statement in statements:
            if not isinstance(statement, dict):
                continue
            if "entity_profile" not in statement:
                continue

            statement_id = statement.get("id", "<unknown>")
            linkage = statement.get("linkage")
            if not isinstance(linkage, dict):
                errors.append(
                    f"{profile_name}/profile.yaml statement '{statement_id}': "
                    "'linkage' object is required when 'entity_profile' is present"
                )
                continue

            validate_required_paths(
                linkage,
                [
                    "target_profile",
                    "relationship.type",
                    "relationship.direction",
                    "cardinality.min",
                    "cardinality.max",
                    "workflow_policy.create",
                    "workflow_policy.select_existing",
                    "traversal.max_depth",
                ],
                f"{profile_name}/profile.yaml statement '{statement_id}' linkage",
                errors,
            )

            if linkage.get("target_profile") != statement.get("entity_profile"):
                errors.append(
                    f"{profile_name}/profile.yaml statement '{statement_id}': "
                    "linkage.target_profile must match entity_profile"
                )

            direction = get_nested(linkage, "relationship.direction")
            if direction not in {"unidirectional", "bidirectional"}:
                errors.append(
                    f"{profile_name}/profile.yaml statement '{statement_id}': "
                    "relationship.direction must be 'unidirectional' or 'bidirectional'"
                )

        # Validate metadata profile_graph
        profile_graph = metadata_data.get("profile_graph")
        if not isinstance(profile_graph, dict):
            errors.append(
                f"{profile_name}/metadata.yaml: 'profile_graph' object is required"
            )
            continue

        neighbors = profile_graph.get("neighbors")
        if not isinstance(neighbors, list):
            errors.append(
                f"{profile_name}/metadata.yaml: 'profile_graph.neighbors' must be a list"
            )
            neighbors = []

        edges = profile_graph.get("edges")
        if not isinstance(edges, list):
            errors.append(
                f"{profile_name}/metadata.yaml: 'profile_graph.edges' must be a list"
            )
            edges = []

        related_profiles = metadata_data.get("related_profiles", [])
        if not isinstance(related_profiles, list):
            errors.append(
                f"{profile_name}/metadata.yaml: 'related_profiles' must be a list when present"
            )
            related_profiles = []

        edge_targets: set[str] = set()
        for index, edge in enumerate(edges):
            if not isinstance(edge, dict):
                errors.append(
                    f"{profile_name}/metadata.yaml edge[{index}]: edge must be an object"
                )
                continue

            validate_required_paths(
                edge,
                [
                    "target_profile",
                    "via_statement",
                    "relationship_type",
                    "cardinality.min",
                    "cardinality.max",
                    "traversal.max_depth",
                ],
                f"{profile_name}/metadata.yaml edge[{index}]",
                errors,
            )

            target_profile = edge.get("target_profile")
            via_statement = edge.get("via_statement")
            if isinstance(target_profile, str):
                edge_targets.add(target_profile)
                if not (profiles_root / target_profile).exists():
                    errors.append(
                        f"{profile_name}/metadata.yaml edge[{index}]: "
                        f"target_profile '{target_profile}' does not exist"
                    )

            if isinstance(via_statement, str) and via_statement not in statement_ids:
                errors.append(
                    f"{profile_name}/metadata.yaml edge[{index}]: "
                    f"via_statement '{via_statement}' is not a statement id in {profile_name}/profile.yaml"
                )

        if set(neighbors) != edge_targets:
            errors.append(
                f"{profile_name}/metadata.yaml: neighbors must exactly match edge target profiles"
            )

        if set(related_profiles) != edge_targets:
            errors.append(
                f"{profile_name}/metadata.yaml: related_profiles must exactly match edge target profiles"
            )

    # Validate bidirectional awareness at metadata graph level
    for profile_name, metadata_data in metadata_by_profile.items():
        profile_graph = metadata_data.get("profile_graph", {})
        edges = profile_graph.get("edges", []) if isinstance(profile_graph, dict) else []
        for edge in edges:
            if not isinstance(edge, dict):
                continue
            target_profile = edge.get("target_profile")
            if not isinstance(target_profile, str):
                continue
            target_metadata = metadata_by_profile.get(target_profile)
            if not isinstance(target_metadata, dict):
                continue
            target_graph = target_metadata.get("profile_graph", {})
            target_edges = target_graph.get("edges", []) if isinstance(target_graph, dict) else []
            has_reverse = any(
                isinstance(target_edge, dict)
                and target_edge.get("target_profile") == profile_name
                for target_edge in target_edges
            )
            if not has_reverse:
                errors.append(
                    f"{profile_name}/metadata.yaml: expected reciprocal edge from {target_profile} back to {profile_name}"
                )

    if errors:
        print("❌ Linkage/profile graph validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("✅ Linkage/profile graph validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
