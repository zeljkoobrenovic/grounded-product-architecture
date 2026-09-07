#!/bin/zsh
set -uo pipefail

# Regenerate docs for every registered product domain.
#
# The domain registry is the config tree itself: every
# _config/product-domains/<group>/<id>/start/config.json (with id/name/description)
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
  "generate-residuality-docs.py"
)

failures=()

# Resolve through the shared registry so changing groups needs no script edits.
domain_ids="$(python3 ../domain_paths.py list)" || exit 1
if [[ -z "$domain_ids" ]]; then
  echo "No registered product domains found in the source groups." >&2
  exit 1
fi

for domain_id in "${(@f)domain_ids}"; do
  domain_dir="$(python3 ../domain_paths.py resolve "$domain_id")" || exit 1
  config="$domain_dir/start/config.json"
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
