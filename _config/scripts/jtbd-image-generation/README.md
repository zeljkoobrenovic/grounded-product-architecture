# JTBD Image Generation

This folder contains a source-first script that scans product-domain customer models, generates job-to-be-done imagery, saves files into each domain's `customers/media/` folder, and updates `customers.json` media references when needed.

## What It Does

- finds every `_config/product-domains/<domain-id>/customers/customers.json`
- reads every customer, job-to-be-done, and step
- builds a better image prompt from:
  - customer name and description
  - JTBD name, outcome, and description
  - step text and capability mappings
  - the style cues from `_prompts/customers/jtbd-cartoon-prompt.txt`
- calls the OpenAI Images API
- writes image files into `customers/media/`
- patches `media` entries in JSON if missing or stale

## Requirements

- Python 3.10+
- `OPENAI_API_KEY` in the environment
- outbound network access when you actually run the script

The script uses only Python's standard library. No extra package install is required.

## Usage

From the repository root:

```bash
export OPENAI_API_KEY=...
python3 _config/scripts/jtbd-image-generation/generate_jtbd_images.py --dry-run
python3 _config/scripts/jtbd-image-generation/generate_jtbd_images.py --domain nutrition --limit 4
python3 _config/scripts/jtbd-image-generation/generate_jtbd_images.py --domain nutrition --overwrite
```

Useful flags:

- `--domain <id>` limits work to one domain
- `--limit N` caps the number of generated images
- `--skip-existing` avoids regenerating files already on disk
- `--overwrite` regenerates image files even if they already exist
- `--json-only` updates missing `media` references without calling the API
- `--dry-run` prints planned actions only
- `--model` defaults to `gpt-image-1`

## Notes

- The script updates only `customers/customers.json`. It does not regenerate `docs/`.
- Existing non-image mediopen-ai-key
- a entries are preserved.
- Existing user changes elsewhere in the worktree are untouched.
