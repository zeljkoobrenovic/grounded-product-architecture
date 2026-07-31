#!/bin/bash

set -eu

cd "$(dirname "$0")"

# The per-source generators are examples: they read external inputs (e.g.
# <repo>/data/sokrates/..., Workday/GCP/AWS exports) that are not part of this
# repository. Run each one only when it succeeds; otherwise keep the committed
# fragment files under database/evidence-files/ as-is.
for script in \
  _example_scripts/source-code/generate-source-code-evidence.sh \
  _example_scripts/gcp/generate-gcp-evidence.sh \
  _example_scripts/aws/generate-aws-evidence.sh \
  _example_scripts/workday/generate-workday-evidence.sh; do
  if bash "$script" 2>/dev/null; then
    echo "Refreshed evidence via $script"
  else
    echo "Skipped $script (input data not available); keeping committed fragments"
  fi
done

python3 database/aggregate-evidence.py

# Regenerate the static Evidence Explorer page from the aggregated database.
python3 ../_wiring/evidence-explorer/generate-evidence-explorer-docs.py
