#!/bin/bash
set -euo pipefail

defaultBaseUrl="https://fingerprintjs.github.io/fingerprint-pro-server-api-openapi"
schemaUrl="${1:-$defaultBaseUrl/schemas/fingerprint-server-api-v4.yaml}"
examplesBaseUrl="${2:-$defaultBaseUrl/examples}"

mkdir -p ./res

curl -fSL --retry 3 -o ./res/fingerprint-server-api.yaml "$schemaUrl"

examples=(
  'events/search/get_event_search_200.json'
  'webhook/webhook_event.json'
  'events/get_event_200.json'
  'events/get_event_ruleset_200.json'
  'events/update_event_multiple_fields_request.json'
  'events/update_event_one_field_request.json'
  'errors/400_visitor_id_required.json'
  'errors/400_visitor_id_invalid.json'
  'errors/403_feature_not_enabled.json'
  'errors/403_secret_api_key_not_found.json'
  'errors/403_secret_api_key_required.json'
  'errors/403_wrong_region.json'
  'errors/404_visitor_not_found.json'
  'errors/429_too_many_requests.json'
)

baseDestination="./test/mocks"
mkdir -p "$baseDestination"

for example in "${examples[@]}"; do
  destinationPath="$baseDestination/$example"
  destinationDir="$(dirname "$destinationPath")"
  mkdir -p "$destinationDir"

  exampleUrl="$examplesBaseUrl/$example"
  echo "Downloading $exampleUrl to $destinationPath"
  curl -fSL --retry 3 -o "$destinationPath" "$exampleUrl"
done

./generate.sh
