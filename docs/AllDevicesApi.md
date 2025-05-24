# nrf_cloud_client.AllDevicesApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device**](AllDevicesApi.md#delete_device) | **DELETE** /devices/{deviceId} | DeleteDevice
[**delete_device_image**](AllDevicesApi.md#delete_device_image) | **DELETE** /devices/{deviceId}/image | DeleteDeviceImage
[**fetch_device**](AllDevicesApi.md#fetch_device) | **GET** /devices/{deviceId} | FetchDevice
[**list_device_tags**](AllDevicesApi.md#list_device_tags) | **GET** /devices/tags | ListDeviceTags
[**list_devices**](AllDevicesApi.md#list_devices) | **GET** /devices | ListDevices
[**update_device_image**](AllDevicesApi.md#update_device_image) | **PUT** /devices/{deviceId}/image | UpdateDeviceImage
[**update_device_name**](AllDevicesApi.md#update_device_name) | **PUT** /devices/{deviceId}/name | UpdateDeviceName
[**update_device_tags**](AllDevicesApi.md#update_device_tags) | **PUT** /devices/{deviceId}/tags | UpdateDeviceTags


# **delete_device**
> delete_device(device_id, body=body)

DeleteDevice

Delete a device from your account. If you are attempting to delete a Nordic hardware product that was [onboarded](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Associations/Onboarding.html) but not yet added to your account (associated), you must also pass the ownership code (PIN or HWID on the product label) in the request body.
This will forward a DEVICE DISCON message on the /c2d MQTT topic, allowing the device to gracefully disconnect. You can [view the format here](https://github.com/nRFCloud/application-protocols/tree/v1/schemas/cloudToDevice/device).
```sh
curl -X DELETE $API_HOST/v1/devices/$DEVICE_ID -d $DEVICE_OWNERSHIP_CODE -H "Authorization: Bearer $API_KEY" -H "Content-Type: text/plain"
```

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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # DeleteDevice
        api_instance.delete_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling AllDevicesApi->delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_image**
> delete_device_image(device_id)

DeleteDeviceImage

For a Web URL of an image associated with a device, dissociate the URL from the device. For an image file stored for a device, delete the image file.

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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # DeleteDeviceImage
        api_instance.delete_device_image(device_id)
    except Exception as e:
        print("Exception when calling AllDevicesApi->delete_device_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

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

# **fetch_device**
> FetchDevice200Response fetch_device(device_id, transform=transform)

FetchDevice

Fetch a device and its state.
```sh
curl $API_HOST/v1/devices/$DEVICE_ID -H "Authorization: Bearer $API_KEY"
```

### Example

* Bearer Authentication (Simple Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.fetch_device200_response import FetchDevice200Response
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

# Configure Bearer authorization: JSON Web Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    transform = ['transform_example'] # List[str] | Not a true array of strings, but rather a JSONata expression such as `id` or `{ \"id\": id, \"type\": type }`. For more information see [Transforming JSON Responses guide](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/Tutorials/Transforms.html). (optional)

    try:
        # FetchDevice
        api_response = api_instance.fetch_device(device_id, transform=transform)
        print("The response of AllDevicesApi->fetch_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllDevicesApi->fetch_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **transform** | [**List[str]**](str.md)| Not a true array of strings, but rather a JSONata expression such as &#x60;id&#x60; or &#x60;{ \&quot;id\&quot;: id, \&quot;type\&quot;: type }&#x60;. For more information see [Transforming JSON Responses guide](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/Tutorials/Transforms.html). | [optional] 

### Return type

[**FetchDevice200Response**](FetchDevice200Response.md)

### Authorization

[Simple Token](../README.md#Simple Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_device_tags**
> PaginatedResultDeviceTagOrJSONataTransformedResponse list_device_tags(page_limit, page_next_token=page_next_token)

ListDeviceTags

List all device tags (groups) for your account.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_device_tag_or_jso_nata_transformed_response import PaginatedResultDeviceTagOrJSONataTransformedResponse
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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    page_limit = 56 # int | 
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListDeviceTags
        api_response = api_instance.list_device_tags(page_limit, page_next_token=page_next_token)
        print("The response of AllDevicesApi->list_device_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllDevicesApi->list_device_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_limit** | **int**|  | 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultDeviceTagOrJSONataTransformedResponse**](PaginatedResultDeviceTagOrJSONataTransformedResponse.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> PaginatedResultDeviceOrJSONataTransformedResponse list_devices(include_state=include_state, include_state_meta=include_state_meta, transform=transform, page_limit=page_limit, tags=tags, device_ids=device_ids, device_identifiers=device_identifiers, firmware_support=firmware_support, firmware_support_exclude=firmware_support_exclude, ble_firmware_support=ble_firmware_support, device_types=device_types, gateway_id=gateway_id, sub_types=sub_types, device_name_fuzzy=device_name_fuzzy, page_next_token=page_next_token)

ListDevices

Fetch a list of devices associated with the team defined by your API key.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_types import DeviceTypes
from nrf_cloud_client.models.firmware_types import FirmwareTypes
from nrf_cloud_client.models.paginated_result_device_or_jso_nata_transformed_response import PaginatedResultDeviceOrJSONataTransformedResponse
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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    include_state = False # bool | If false (the default), the device’s state is not returned, but only the device metadata. This allows you to keep the response size small if needed. (optional) (default to False)
    include_state_meta = False # bool | If false (the default), the metadata for an IP-based device's state (i.e., timestamps reflecting each property's last updated time) are not returned. (optional) (default to False)
    transform = ['transform_example'] # List[str] | Not a true array of strings, but rather a JSONata expression such as `id` or `{ \"id\": id, \"type\": type }`. For more information see [Transforming JSON Responses guide](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/Tutorials/Transforms.html). (optional)
    page_limit = 56 # int |  (optional)
    tags = ['tags_example'] # List[str] | If specified, only return devices that have one of these tags AND are accessible by the user's Role and their assigned Device Groups (tags) (optional)
    device_ids = ['device_ids_example'] # List[str] | If specified, only return devices with matching identifiers (optional)
    device_identifiers = ['device_identifiers_example'] # List[str] |  (optional)
    firmware_support = [nrf_cloud_client.FirmwareTypes()] # List[FirmwareTypes] | If specified, only return devices that support the given firmware types (optional)
    firmware_support_exclude = [nrf_cloud_client.FirmwareTypes()] # List[FirmwareTypes] |  (optional)
    ble_firmware_support = True # bool |  (optional)
    device_types = [nrf_cloud_client.DeviceTypes()] # List[DeviceTypes] |  (optional)
    gateway_id = 'gateway_id_example' # str |  (optional)
    sub_types = ['sub_types_example'] # List[str] |  (optional)
    device_name_fuzzy = 'device_name_fuzzy_example' # str |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListDevices
        api_response = api_instance.list_devices(include_state=include_state, include_state_meta=include_state_meta, transform=transform, page_limit=page_limit, tags=tags, device_ids=device_ids, device_identifiers=device_identifiers, firmware_support=firmware_support, firmware_support_exclude=firmware_support_exclude, ble_firmware_support=ble_firmware_support, device_types=device_types, gateway_id=gateway_id, sub_types=sub_types, device_name_fuzzy=device_name_fuzzy, page_next_token=page_next_token)
        print("The response of AllDevicesApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllDevicesApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_state** | **bool**| If false (the default), the device’s state is not returned, but only the device metadata. This allows you to keep the response size small if needed. | [optional] [default to False]
 **include_state_meta** | **bool**| If false (the default), the metadata for an IP-based device&#39;s state (i.e., timestamps reflecting each property&#39;s last updated time) are not returned. | [optional] [default to False]
 **transform** | [**List[str]**](str.md)| Not a true array of strings, but rather a JSONata expression such as &#x60;id&#x60; or &#x60;{ \&quot;id\&quot;: id, \&quot;type\&quot;: type }&#x60;. For more information see [Transforming JSON Responses guide](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/Tutorials/Transforms.html). | [optional] 
 **page_limit** | **int**|  | [optional] 
 **tags** | [**List[str]**](str.md)| If specified, only return devices that have one of these tags AND are accessible by the user&#39;s Role and their assigned Device Groups (tags) | [optional] 
 **device_ids** | [**List[str]**](str.md)| If specified, only return devices with matching identifiers | [optional] 
 **device_identifiers** | [**List[str]**](str.md)|  | [optional] 
 **firmware_support** | [**List[FirmwareTypes]**](FirmwareTypes.md)| If specified, only return devices that support the given firmware types | [optional] 
 **firmware_support_exclude** | [**List[FirmwareTypes]**](FirmwareTypes.md)|  | [optional] 
 **ble_firmware_support** | **bool**|  | [optional] 
 **device_types** | [**List[DeviceTypes]**](DeviceTypes.md)|  | [optional] 
 **gateway_id** | **str**|  | [optional] 
 **sub_types** | [**List[str]**](str.md)|  | [optional] 
 **device_name_fuzzy** | **str**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultDeviceOrJSONataTransformedResponse**](PaginatedResultDeviceOrJSONataTransformedResponse.md)

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

# **update_device_image**
> update_device_image(device_id, source_url=source_url, body=body)

UpdateDeviceImage

Update the image associated with a device, as displayed on nrfCloud.com. If uploading an image, add image to the request body (JPEG or PNG only). Otherwise, use the `sourceUrl` query param to set the device image to an existing image on the Web.

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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    source_url = 'source_url_example' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # UpdateDeviceImage
        api_instance.update_device_image(device_id, source_url=source_url, body=body)
    except Exception as e:
        print("Exception when calling AllDevicesApi->update_device_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **source_url** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_name**
> update_device_name(device_id, body)

UpdateDeviceName

Update the device name. The default name is the same as the device id.

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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str | 

    try:
        # UpdateDeviceName
        api_instance.update_device_name(device_id, body)
    except Exception as e:
        print("Exception when calling AllDevicesApi->update_device_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_tags**
> update_device_tags(device_id, request_body)

UpdateDeviceTags

Update a device's tags. Useful for labeling, categorizing, grouping, etc.

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
    api_instance = nrf_cloud_client.AllDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    request_body = ['request_body_example'] # List[str] | 

    try:
        # UpdateDeviceTags
        api_instance.update_device_tags(device_id, request_body)
    except Exception as e:
        print("Exception when calling AllDevicesApi->update_device_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

