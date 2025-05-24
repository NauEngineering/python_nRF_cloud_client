SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR"

openapi-generator-cli generate -i https://api.nrfcloud.com/v1/openapi.json -o .. --generator-name python --skip-validate-spec \
    --package-name nrf_cloud_client --additional-properties=packageVersion=0.0.1,packageUrl=https://github.com/NauEngineering/python_nRF_cloud_client \
    --git-user-id=NauEngineering --git-repo-id=python_nRF_cloud_client