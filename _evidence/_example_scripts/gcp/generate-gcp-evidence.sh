#!/usr/bin/env sh

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

python3 "$SCRIPT_DIR/generate-gcp-evidence.py" \
  --input "$SCRIPT_DIR/../../../data/gcp/data/json/projects.json" \
  --output "$SCRIPT_DIR/../../database/evidence-files/gcp-projects.json"
