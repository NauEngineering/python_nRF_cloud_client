# nrf_cloud_client.FirmwareBundlesApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_firmware**](FirmwareBundlesApi.md#delete_firmware) | **DELETE** /firmwares/{bundleId} | DeleteFirmware
[**list_firmware**](FirmwareBundlesApi.md#list_firmware) | **GET** /firmwares | ListFirmware
[**upload_firmware**](FirmwareBundlesApi.md#upload_firmware) | **POST** /firmwares | UploadFirmware


# **delete_firmware**
> delete_firmware(bundle_id)

DeleteFirmware

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.FirmwareBundlesApi(api_client)
    bundle_id = None # object | 

    try:
        # DeleteFirmware
        api_instance.delete_firmware(bundle_id)
    except Exception as e:
        print("Exception when calling FirmwareBundlesApi->delete_firmware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firmware**
> PaginatedResultFirmware list_firmware(page_next_token=page_next_token, page_limit=page_limit, modem_only=modem_only)

ListFirmware

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_firmware import PaginatedResultFirmware
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.FirmwareBundlesApi(api_client)
    page_next_token = 'page_next_token_example' # str |  (optional)
    page_limit = 56 # int |  (optional)
    modem_only = False # bool | Whether or not to return a list of modem firmware instead of the current tenant's firmware (optional) (default to False)

    try:
        # ListFirmware
        api_response = api_instance.list_firmware(page_next_token=page_next_token, page_limit=page_limit, modem_only=modem_only)
        print("The response of FirmwareBundlesApi->list_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirmwareBundlesApi->list_firmware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_next_token** | **str**|  | [optional] 
 **page_limit** | **int**|  | [optional] 
 **modem_only** | **bool**| Whether or not to return a list of modem firmware instead of the current tenant&#39;s firmware | [optional] [default to False]

### Return type

[**PaginatedResultFirmware**](PaginatedResultFirmware.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_firmware**
> UploadFirmware202Response upload_firmware(content_type, body)

UploadFirmware

Upload a firmware bundle as a .zip file, whether binary or base64-encoded. The bundle must contain a manifest.json file that conforms to this JSON schema:
```
{
   name?: string,
   description?: string,
   fwversion: string,
   'format-version': 1,
   files: {
     file: string,
     type: 'application' | 'mcuboot' | 'bootloader' | 'softdevice' | 'init_packet',
     size: number
   }[]
 }
```
Notes:
- `?` fields are optional
- `files` is an array of objects, all of which should be of the same `type`.
- `file` must have a `.bin` extension. Host-side tools like [nRF Connect for Desktop Programmer](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop) can be used to convert `.hex` files to `.bin`.
- `type` values `application` and `mcuboot` apply only to nRF91 FOTA. Values `softdevice` and `init_packet` apply only to Bluetooth LE FOTA.
- For Bluetooth LE devices using FOTA, the `.zip` file must contain both the init_packet and the firmware image (application or soft device). The `type` field for the manifest must be `application` or `softdevice`, not `init_packet`.
- `'format-version'` should always be set to `1`
- `fwversion` is validated against this regular expression: `/^[a-zA-Z0-9._-]{1,60}$/`
- The Zephyr build system produces dfu_application.zip in the build/zephyr folder, which contains a manifest.json plus the update binary. However, the manifest is currently generated without the required `fwversion` field, so you will need to add that field.
- If you use the nRFCloud.com user interface to upload your zip file, you are given options to fill in the `name`, `description`, and `fwversion` fields. The UI will then properly generate the manifest.json file and zip file.
- Although nRF Cloud supports modem FOTA, we do not allow uploading modem firmware. These updates are made available only by Nordic Semiconductor.

An example of a valid manifest:
```
{
   "name": "My application update",
   "description": "Changelog: Fixed an issue with sleep mode. Power consumption improvements.",
   "fwversion": "1.1",
   "format-version": 1,
   "files": [
       {
           "file": "my_application_v1_1.hex.bin",
           "type": "application",
           "size": 695672
       }
   ]
}
```
Following are examples of uploading with curl (base64 and binary):

Using base64 encoded content:
```sh
export FILE=$(base64 path/to/my-file.zip)
# If you get a console error such as "Argument list too long" try using a REST client like Postman.

# UTF-8
curl -X POST $API_HOST/v1/firmwares \
   -H "Authorization: Bearer $API_KEY" \
   -H "Content-Type: text/plain;charset=UTF8" \
   -d $FILE

# ASCII
curl -X POST $API_HOST/v1/firmwares \
   -H "Authorization: Bearer $API_KEY" \
   -H "Content-Type: text/plain;charset=ASCII" \
   -d $FILE

# Plain Text
curl -X POST $API_HOST/v1/firmwares \
   -H "Authorization: Bearer $API_KEY" \
   -H "Content-Type: text/plain" \
   -d $FILE
```
Using binary content:
```sh
# Octet-stream
curl -X POST $API_HOST/v1/firmwares \
   -H "Authorization: Bearer $API_KEY" \
   -H "Content-Type: application/octet-stream" \
   --data-binary @/path/to/my-file.zip

# ZIP
curl -X POST $API_HOST/v1/firmwares \
   -H "Authorization: Bearer $API_KEY" \
   -H "Content-Type: application/zip" \
   --data-binary @/path/to/my-file.zip
```
For more information, see the [FOTA documentation](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/FirmwareUpdate/FOTAOverview.html).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.rest_api_payload_content_type_with_zip import RestApiPayloadContentTypeWithZip
from nrf_cloud_client.models.upload_firmware202_response import UploadFirmware202Response
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.FirmwareBundlesApi(api_client)
    content_type = nrf_cloud_client.RestApiPayloadContentTypeWithZip() # RestApiPayloadContentTypeWithZip | 
    body = 'body_example' # str | 

    try:
        # UploadFirmware
        api_response = api_instance.upload_firmware(content_type, body)
        print("The response of FirmwareBundlesApi->upload_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirmwareBundlesApi->upload_firmware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | [**RestApiPayloadContentTypeWithZip**](.md)|  | 
 **body** | **str**|  | 

### Return type

[**UploadFirmware202Response**](UploadFirmware202Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

