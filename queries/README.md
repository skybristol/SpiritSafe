# This directory contains shared SPARQL queries used across multiple profiles
#
# Profile-specific queries should be placed in profiles/[ProfileName]/queries/
#
# Query File Format:
#   - File extension: .sparql
#   - Comments: Lines starting with # are treated as metadata
#   - Parameters: Use {{param_name}} syntax for hydration-time substitution
#   - Expected vars: Document as comment (e.g., # Expected vars: ?item ?itemLabel)
#
# Example parameter comment:
#   # Parameters (string replacement by hydration tooling):
#   #   {{class_qid}} default Q5
#   #   {{lang}} default en
#
# The hydrate-caches.yml workflow parses these comments to extract default
# parameter values for query execution.
