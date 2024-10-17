#!/bin/bash

tox -e py37 -- --mpl-generate-path=tests/baseline

tox -e py37 -- --mpl-generate-hash-library=tests/image_hashes_37.json
tox -e py38 -- --mpl-generate-hash-library=tests/image_hashes_38.json
tox -e py39 -- --mpl-generate-hash-library=tests/image_hashes.json
# tox -e py313 -- --mpl-generate-hash-library=image_hashes_313.json

python3 sort_hashes_json.py
