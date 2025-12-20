#!/bin/bash
# Removes tenant-specific fields from Sentinel workbook JSON files
# Usage: ./strip-workbook-ids.sh <workbook.json>

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <workbook.json>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File not found: $1"
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "Error: jq is required. Install with: sudo apt install jq"
    exit 1
fi

jq 'del(.fallbackResourceIds, .context) | walk(if type == "object" then del(.id, .crossComponentResources) else . end)' "$1" > "$1.tmp" && mv "$1.tmp" "$1"
echo "Stripped tenant-specific fields from $1"