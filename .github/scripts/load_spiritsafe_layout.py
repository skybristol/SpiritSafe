from pathlib import Path

import yaml


DEFAULTS = {
    "entities": "cache/entities",
    "profiles": "profiles",
    "value_list_queries": "queries",
    "value_list_cache": "cache/queries",
    "semantic_anchors": "config/semantic_anchors.json",
    "logs": "cache/refresh",
    "wikimedia_sites": "cache/config/wikimedia_sites.json",
    "manifest": "cache/manifest.json",
    "entity_index": "cache/entity_index.json",
}


def main() -> None:
    config_path = Path("config/dd-wikibase.yaml")
    paths = dict(DEFAULTS)

    if config_path.exists():
        raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        spiritsafe = raw.get("spiritsafe") or {}
        configured_paths = spiritsafe.get("paths") or {}
        for key, default in DEFAULTS.items():
            value = configured_paths.get(key)
            if isinstance(value, str) and value.strip():
                paths[key] = value.strip()
            else:
                paths[key] = default

    print(f"SPIRITSAFE_ENTITIES_PATH={paths['entities']}")
    print(f"SPIRITSAFE_PROFILES_PATH={paths['profiles']}")
    print(f"SPIRITSAFE_VALUE_LIST_QUERIES_PATH={paths['value_list_queries']}")
    print(f"SPIRITSAFE_VALUE_LIST_CACHE_PATH={paths['value_list_cache']}")
    print(f"SPIRITSAFE_SEMANTIC_ANCHORS_PATH={paths['semantic_anchors']}")
    print(f"SPIRITSAFE_LOGS_PATH={paths['logs']}")
    print(f"SPIRITSAFE_WIKIMEDIA_SITES_PATH={paths['wikimedia_sites']}")
    print(f"SPIRITSAFE_MANIFEST_PATH={paths['manifest']}")
    print(f"SPIRITSAFE_ENTITY_INDEX_PATH={paths['entity_index']}")


if __name__ == "__main__":
    main()