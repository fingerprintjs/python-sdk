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

# jar was downloaded from here https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.34/

find ./docs -type f ! -name "DecryptionKey.md" ! -name "SealedResults.md" -exec rm {} +
cd fingerprint_server_sdk/models
shopt -s extglob
rm !("error_plain_response.py")
cd ../..
java -jar ./bin/swagger-codegen-cli.jar generate -t ./template -l python -i ./res/fingerprint-server-api.yaml -o ./ -c config.json -DpackageVersion=$VERSION

python ./fix_codegen_problems.py

# Ugly fix for codegen problem that I couldn't fix editing template.
# Platform check
platform=$(uname)
(
  # Readme file fix
  replacement=$(printf 'The rawAttributes object follows this general shape: `{ value: any } | { error: { name: string; message: string; } }`\n')
  readme_filename="./docs/RawDeviceAttributes.md"
  if [ "$platform" = "Darwin" ]; then
    sed -i '' "s/^Name |.*/${replacement}/" "$readme_filename"
    sed -i '' "/^------------ |/c\\" "$readme_filename"
  else
    sed -i "s/^Name |.*/${replacement}/" "$readme_filename"
    sed -i "/^------------ |/c\\" "$readme_filename"
  fi
)

# Replace version in other files
(
  if [ "$platform" = "Darwin" ]; then
    sed -i '' "s/^VERSION = '[^']*'/VERSION = '${VERSION}'/" "./test/test_fingerprint_api.py"
    sed -i '' "s/^version = [^']*/version = ${VERSION}/" "./setup.cfg"
  else
    sed -i "s/^VERSION = '[^']*'/VERSION = '${VERSION}'/" "./test/test_fingerprint_api.py"
    sed -i "s/^version = [^']*/version = ${VERSION}/" "./setup.cfg"
  fi
)
