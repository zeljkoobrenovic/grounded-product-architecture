#!/usr/bin/env sh

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

python3 "$SCRIPT_DIR/generate-domain-objectives-evidence.py" \
  --input-root "$SCRIPT_DIR/../../../data/domain-specific/objectives" \
  --output "$SCRIPT_DIR/../../database/evidence-files/domain-objectives.json"
