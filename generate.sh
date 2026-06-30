#!/bin/bash

if ! docker info > /dev/null 2>&1; then
  echo "Error: Docker is not running. Please start Docker and try again."
  exit 1
fi

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

docker run --rm -u "$(id -u):$(id -g)" -v "${PWD}:/local" -w /local "openapitools/openapi-generator-cli:${OPENAPI_GENERATOR_IMAGE_VERSION}" generate \
  -i ./res/fingerprint-server-api.yaml \
  -g python \
  -o ./ \
  -t ./template \
  -c ./config.json \
  --additional-properties=packageVersion="$VERSION"

if [ $? -ne 0 ]; then
  echo "Error: Code generation failed."
  exit 1
fi

# Linting and formatting
uv run ruff format .
uv run ruff check --fix --unsafe-fixes .

