#!/usr/bin/env sh

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

python3 "$SCRIPT_DIR/generate-repositories.py" \
  --input "$SCRIPT_DIR/../raw-data/sokrates/repositories.json" \
  --output "$SCRIPT_DIR/source-code/repositories.json"
