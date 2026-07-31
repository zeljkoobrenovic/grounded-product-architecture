#!/bin/zsh
set -uo pipefail

# Regenerate docs for every registered product domain.
#
# The domain registry is the config tree itself: every
# _config/product-domains/<id>/start/config.json (with id/name/description)
# is a registered domain. To add a domain, create its config folder — there
# is no separate list to maintain here.
#
# Failures are isolated per domain+generator: the run continues and reports
# every failure at the end, exiting non-zero if any occurred.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

scripts=(
  "generate-start-docs.py"
  "generate-customers-docs.py"
  "generate-products-docs.py"
  "generate-product-bricks-docs.py"
  "generate-teams-docs.py"
  "generate-competition-docs.py"
)

domains_root="../../_config/product-domains"
failures=()

for config in "$domains_root"/*/start/config.json; do
  [ -f "$config" ] || continue
  domain_id="$(basename "$(dirname "$(dirname "$config")")")"
  domain_name="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['name'])" "$config")"
  domain_description="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['description'])" "$config")"

  for script in "${scripts[@]}"; do
    if ! python3 "$script" "$domain_id" "$domain_name" "$domain_description" > /dev/null; then
      failures+=("$domain_id/$script")
      echo "FAILED: $domain_id $script" >&2
    fi
  done
done

if (( ${#failures[@]} > 0 )); then
  echo ""
  echo "Generation finished with ${#failures[@]} failure(s):" >&2
  for failure in "${failures[@]}"; do
    echo "  - $failure" >&2
  done
  exit 1
fi

echo "All domains generated successfully."
