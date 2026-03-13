#!/bin/bash
set -euo pipefail

defaultBaseUrl="https://fingerprintjs.github.io/fingerprint-pro-server-api-openapi"
schemaUrl="${1:-$defaultBaseUrl/schemas/fingerprint-server-api-compact.yaml}"

mkdir -p ./res

curl -fSL --retry 3 -o ./res/fingerprint-server-api.yaml "$schemaUrl"

./generate.sh
