#!/bin/bash

VERSION=$(jq -r '.version' package.json)

while getopts "v:" arg; do
  case $arg in
    v)
      VERSION=$OPTARG
      ;;
  esac
done

# Make prerelease version compatible with PEP 440
if [[ $VERSION =~ (.*-test\.)([0-9]+) ]]; then
  BASE_VERSION=${BASH_REMATCH[1]}
  DEV_NUMBER=${BASH_REMATCH[2]}
  VERSION="${BASE_VERSION%-rc.}.rc${DEV_NUMBER}"
fi

# Cleanup
rm -Rf fingerprint_server_sdk
rm -Rf docs

OPENAPI_GENERATOR_IMAGE_VERSION="v7.19.0"

docker run --rm -v "${PWD}:/local" -w /local "openapitools/openapi-generator-cli:${OPENAPI_GENERATOR_IMAGE_VERSION}" generate \
  -i ./res/fingerprint-server-api.yaml \
  -g python \
  -o ./ \
  -t ./template \
  -c ./config.json \
  --additional-properties=packageVersion="$VERSION"

# Linting and formatting
PYTHON_CMD="${PYTHON:-$(command -v python3 || command -v python)}"
"$PYTHON_CMD" -m ruff format .
"$PYTHON_CMD" -m ruff check --fix --unsafe-fixes .