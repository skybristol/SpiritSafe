#!/usr/bin/env python3
"""
Build SpiritSafe registry manifest.

This script generates a comprehensive JSON manifest that indexes all profiles
in the SpiritSafe registry, including their metadata, queries, and cache locations.
The manifest serves as the authoritative registry for the gkc package and other
tools that consume SpiritSafe profiles.

Usage:
  python build-manifest.py [--output path/to/manifest.json]
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
import subprocess
import yaml


def get_commit_info() -> Dict[str, str]:
    """Get current commit SHA and timestamp."""
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=Path(__file__).parent.parent.parent,
            text=True
        ).strip()
        
        # Get commit timestamp
        timestamp = subprocess.check_output(
            ["git", "log", "-1", "--format=%aI"],
            cwd=Path(__file__).parent.parent.parent,
            text=True
        ).strip()
        
        return {"commit_sha": sha, "commit_timestamp": timestamp}
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fallback if git is not available
        return {
            "commit_sha": "unknown",
            "commit_timestamp": datetime.now(timezone.utc).isoformat()
        }


def discover_profiles(repo_root: Path) -> List[Path]:
    """Discover all profile directories (those with profile.yaml and metadata.yaml)."""
    profiles_dir = repo_root / "profiles"
    if not profiles_dir.exists():
        return []
    
    profile_dirs = []
    for item in profiles_dir.iterdir():
        if item.is_dir():
            if (item / "profile.yaml").exists() and (item / "metadata.yaml").exists():
                profile_dirs.append(item)
    
    return sorted(profile_dirs)


def load_metadata(metadata_path: Path) -> Dict[str, Any]:
    """Load and parse metadata.yaml file."""
    try:
        with open(metadata_path, "r") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Warning: Failed to load {metadata_path}: {e}", file=sys.stderr)
        return {}


def discover_queries(profile_dir: Path) -> List[Dict[str, str]]:
    """Discover SPARQL query files in profile's queries directory."""
    queries_dir = profile_dir / "queries"
    queries = []
    
    if queries_dir.exists():
        for query_file in sorted(queries_dir.glob("*.sparql")):
            query_name = query_file.stem
            source_path = query_file.relative_to(profile_dir.parent.parent)
            cache_path = (
                Path("cache") / "profiles" / profile_dir.name / f"{query_name}.json"
            )
            
            queries.append({
                "filename": query_file.name,
                "source_path": str(source_path),
                "cache_path": str(cache_path)
            })
    
    return queries


def build_profile_entry(
    profile_dir: Path, repo_root: Path
) -> Dict[str, Any]:
    """Build manifest entry for a single profile."""
    profile_id = profile_dir.name
    metadata = load_metadata(profile_dir / "metadata.yaml")
    
    # Paths relative to repo root
    rel_root = profile_dir.relative_to(repo_root)
    
    entry: Dict[str, Any] = {
        "id": profile_id,
        "name": metadata.get("name", profile_id),
        "description": metadata.get("description", ""),
        "version": metadata.get("version", "unknown"),
        "status": metadata.get("status", "unknown"),
    }
    
    # Add optional fields if present
    if "authors" in metadata:
        entry["authors"] = metadata["authors"]
    if "maintainers" in metadata:
        entry["maintainers"] = metadata["maintainers"]
    if "published_date" in metadata:
        # Convert date to ISO string if needed
        published_date = metadata["published_date"]
        if hasattr(published_date, "isoformat"):
            entry["published_date"] = published_date.isoformat()
        else:
            entry["published_date"] = str(published_date)
    if "related_profiles" in metadata:
        entry["related_profiles"] = metadata["related_profiles"]
    
    # File references
    entry["files"] = {
        "profile_yaml": str(rel_root / "profile.yaml"),
        "metadata_yaml": str(rel_root / "metadata.yaml"),
    }
    
    if (profile_dir / "README.md").exists():
        entry["files"]["readme"] = str(rel_root / "README.md")
    if (profile_dir / "CHANGELOG.md").exists():
        entry["files"]["changelog"] = str(rel_root / "CHANGELOG.md")
    
    # Query files
    queries = discover_queries(profile_dir)
    if queries:
        entry["queries"] = queries
    
    # Cache directory
    entry["cache_directory"] = f"cache/profiles/{profile_id}/"
    
    return entry


def build_manifest(repo_root: Path) -> Dict[str, Any]:
    """Build complete manifest."""
    commit_info = get_commit_info()
    
    profiles = discover_profiles(repo_root)
    profile_entries = []
    
    for profile_dir in profiles:
        try:
            entry = build_profile_entry(profile_dir, repo_root)
            profile_entries.append(entry)
        except Exception as e:
            print(f"Warning: Failed to build entry for {profile_dir}: {e}", file=sys.stderr)
    
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "commit_sha": commit_info["commit_sha"],
        "commit_timestamp": commit_info["commit_timestamp"],
        "profiles": profile_entries,
    }
    
    return manifest


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Build SpiritSafe registry manifest"
    )
    parser.add_argument(
        "--output",
        default="cache/manifest.json",
        help="Output path for manifest (default: cache/manifest.json)"
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to repository root (default: current directory)"
    )
    
    args = parser.parse_args()
    
    repo_root = Path(args.repo_root).resolve()
    
    if not repo_root.exists():
        print(f"Error: Repository root not found: {repo_root}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Building manifest for: {repo_root}")
    manifest = build_manifest(repo_root)
    
    output_path = repo_root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✓ Manifest written to: {output_path}")
    print(f"  Profiles indexed: {len(manifest['profiles'])}")
    for profile in manifest["profiles"]:
        query_count = len(profile.get("queries", []))
        print(f"    - {profile['id']} (v{profile['version']}, {query_count} queries)")


if __name__ == "__main__":
    main()
