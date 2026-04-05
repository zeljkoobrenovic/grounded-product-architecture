#!/usr/bin/env sh

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

python3 "$SCRIPT_DIR/generate-aws-evidence.py" \
  --input "$SCRIPT_DIR/../../../data/aws/data/json/accounts.json" \
  --output "$SCRIPT_DIR/../../database/evidence-files/aws-accounts.json"
