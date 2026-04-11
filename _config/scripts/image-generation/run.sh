#!/bin/bash

python3 generate_missing_domain_icons_gemini_nanobanana_api.py --domain $1
python3 generate_jtbd_images_gemini_nanobanana_api.py --domain $1
python3 generate_journey_images_gemini_nanobanana_api.py --domain $1