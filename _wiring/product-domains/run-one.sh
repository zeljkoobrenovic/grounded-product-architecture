#!/bin/zsh
set -euo pipefail

# Regenerate all docs for a single domain: ./run-one.sh <domain-id>
# Name and description are read from the domain's start/config.json, so they
# can never drift from the registered domain data.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

domain_id="${1:?Usage: ./run-one.sh <domain-id>}"
config="../../_config/product-domains/${domain_id}/start/config.json"

if [[ ! -f "$config" ]]; then
  echo "No such domain config: $config" >&2
  exit 1
fi

domain_name="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['name'])" "$config")"
domain_description="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['description'])" "$config")"

scripts=(
  "generate-start-docs.py"
  "generate-customers-docs.py"
  "generate-products-docs.py"
  "generate-product-bricks-docs.py"
  "generate-teams-docs.py"
  "generate-competition-docs.py"
  "generate-residuality-docs.py"
)

for script in "${scripts[@]}"; do
  python3 "$script" "$domain_id" "$domain_name" "$domain_description"
done
