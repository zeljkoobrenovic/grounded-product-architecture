#!/usr/bin/env sh

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

python3 "$SCRIPT_DIR/scripts/generate-workday-evidence.py" \
  --input "$SCRIPT_DIR/../data/workday/workday.json" \
  --output "$SCRIPT_DIR/database/workday.json"
