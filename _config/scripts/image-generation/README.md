# Product Domain Image Generation

This folder contains source-first scripts that scan product-domain models, generate supporting imagery, save files beside the relevant source JSON, and update media references when needed.

## What It Does

- finds every `_config/product-domains/<domain-id>/customers/customers.json`
- reads every customer plus:
  - `jobsToBeDone` and their steps
  - `customerJourneyStories` and their stages
- builds a better image prompt from:
  - customer name and description
  - JTBD name, outcome, description, and capability mappings
  - journey summary, linked jobs, and stage narratives
  - the style cues from `_prompts/customers/jtbd-cartoon-prompt.txt` or `_prompts/customers/customer-journeys.md`
- calls either the OpenAI Images API or the Gemini Nano Banana image API for JTBD images, and the Gemini Nano Banana image API for journey images
- writes image files into `customers/media/`
- patches `media` entries in JSON if missing or stale
- supports `--lightweight` JTBD and journey runs that create only job/journey overviews, without creating step/stage targets or media references
- generates one Gemini Nano Banana illustration for every residuality stressor, writes it into `residuality/media/`, and patches the stressor's `media` entry

## Requirements

- Python 3.10+
- `OPENAI_API_KEY` for the OpenAI Images API script
- `GEMINI_API_KEY` or `GOOGLE_API_KEY` for the Gemini Nano Banana script
- outbound network access when you actually run the script

The script uses only Python's standard library. No extra package install is required.

## Usage

From the repository root:

JTBD images via OpenAI Images API:

```bash
export OPENAI_API_KEY=...
python3 _config/scripts/image-generation/generate_jtbd_images_openai_images_api.py --dry-run
python3 _config/scripts/image-generation/generate_jtbd_images_openai_images_api.py --domain food-and-nutrition-product-platform --lightweight
python3 _config/scripts/image-generation/generate_jtbd_images_openai_images_api.py --domain food-and-nutrition-product-platform --limit 4
python3 _config/scripts/image-generation/generate_jtbd_images_openai_images_api.py --domain food-and-nutrition-product-platform --overwrite
```

JTBD images via Gemini Nano Banana API:

```bash
export GEMINI_API_KEY=...
python3 _config/scripts/image-generation/generate_jtbd_images_gemini_nanobanana_api.py --dry-run
python3 _config/scripts/image-generation/generate_jtbd_images_gemini_nanobanana_api.py --domain food-and-nutrition-product-platform --lightweight
python3 _config/scripts/image-generation/generate_jtbd_images_gemini_nanobanana_api.py --domain food-and-nutrition-product-platform --limit 4
python3 _config/scripts/image-generation/generate_jtbd_images_gemini_nanobanana_api.py --domain food-and-nutrition-product-platform --overwrite
```

Customer journey images via Gemini Nano Banana API:

```bash
export GEMINI_API_KEY=...
python3 _config/scripts/image-generation/generate_journey_images_gemini_nanobanana_api.py --dry-run
python3 _config/scripts/image-generation/generate_journey_images_gemini_nanobanana_api.py --domain food-and-nutrition-product-platform --lightweight
python3 _config/scripts/image-generation/generate_journey_images_gemini_nanobanana_api.py --domain bike-mobility --json-only
python3 _config/scripts/image-generation/generate_journey_images_gemini_nanobanana_api.py --domain food-and-nutrition-product-platform --limit 4
python3 _config/scripts/image-generation/generate_journey_images_gemini_nanobanana_api.py --domain food-and-nutrition-product-platform --overwrite
```

Run all image generators for a domain, using lightweight JTBD and journey generation:

```bash
_config/scripts/image-generation/run.sh food-and-nutrition-product-platform --lightweight
```

Residuality stressor images via Gemini Nano Banana API:

```bash
export GEMINI_API_KEY=...
python3 _config/scripts/image-generation/generate_residuality_images_gemini_nanobanana_api.py --dry-run
python3 _config/scripts/image-generation/generate_residuality_images_gemini_nanobanana_api.py --domain ride-sharing-marketplace --limit 2
python3 _config/scripts/image-generation/generate_residuality_images_gemini_nanobanana_api.py --domain ride-sharing-marketplace --overwrite
```

Useful flags:

- `--domain <id>` limits work to one domain
- `--limit N` caps the number of generated images
- `--skip-existing` avoids regenerating files already on disk
- `--overwrite` regenerates image files even if they already exist
- `--json-only` updates missing `media` references without calling the API
- `--lightweight` makes the JTBD and journey generators create only job/journey overview images; it skips individual JTBD steps and journey stages and does not add media references for them
- `--dry-run` prints planned actions only
- `--model` defaults to `gpt-image-1.5` for OpenAI and `gemini-3-pro-image-preview` for Gemini
- `--api-key-env` on the Gemini script lets you switch between `GEMINI_API_KEY` and `GOOGLE_API_KEY`
- `generate_journey_images_gemini_nanobanana_api.py` creates:
  - one image for each `customerJourneyStories[]`
  - one image for each `customerJourneyStories[].stages[]`
- `generate_jtbd_images_*` creates:
  - one image for each `jobsToBeDone[]`
  - one image for each `jobsToBeDone[].steps[]`
- `generate_customer_relations_images_gemini_nanobanana_api.py` creates:
  - one relationship-map illustration per domain from `customers/relations.json`
    (saved as `customers/media/relations-overview.png`, referenced via a top-level
    `media` entry in `relations.json` and shown at the top of the Relations tab;
    the reference is only written once the image exists)
- `generate_residuality_images_gemini_nanobanana_api.py` creates:
  - one landscape illustration per `stressors[]` item
  - files named `residuality/media/stressor-<stressor-id>.<format>` using the image format returned by Gemini
  - an image `media` entry on each generated stressor for the residuality page

## Notes

- Image scripts update only their source JSON files. They do not regenerate `docs/`.
- Existing non-image media entries are preserved.
- Lightweight runs preserve any existing step/stage images and media references; omitting `--lightweight` retains full overview plus detail generation.
- Existing user changes elsewhere in the worktree are untouched.
- A safe first run is `--dry-run` or `--json-only` on one domain before doing full image generation.
