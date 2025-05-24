# nrf_cloud_client.MessagesApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_messages**](MessagesApi.md#list_messages) | **GET** /messages | ListMessages
[**send_device_message**](MessagesApi.md#send_device_message) | **POST** /devices/{deviceId}/messages | SendDeviceMessage


# **list_messages**
> PaginatedResultDeviceMessage list_messages(inclusive_start=inclusive_start, start=start, exclusive_end=exclusive_end, end=end, app_id=app_id, device_id=device_id, topic=topic, page_limit=page_limit, page_sort=page_sort, page_next_token=page_next_token)

ListMessages

Fetch historical device messages.

Currently supported parameter combinations:

`appId + deviceId`

`topic + deviceId`

`appId`

`deviceId`

`topic`

Not supported:

`appId + topic`

`appId + topic + deviceId`

For more information, see our [nRF Cloud documentation on device messages](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/MessagesAndAlerts/DeviceMessages.html).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.page_sort import PageSort
from nrf_cloud_client.models.paginated_result_device_message import PaginatedResultDeviceMessage
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
    api_instance = nrf_cloud_client.MessagesApi(api_client)
    inclusive_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    exclusive_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    app_id = 'app_id_example' # str | Filter returned messages by appId. Primarily used by Asset Tracker, AppId is taken from the \"appId\" property of the message body and is intended to represent the type of data being sent. This can be used to categorize your messages for easy filtering when using the same topic. (optional)
    device_id = 'device_id_example' # str | A device Id to fetch messages for. Can be specified with appId or topic. (optional)
    topic = 'topic_example' # str | Fetch messages for a single topic. Can be specified with deviceId. (optional)
    page_limit = 56 # int |  (optional)
    page_sort = desc # PageSort |  (optional) (default to desc)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListMessages
        api_response = api_instance.list_messages(inclusive_start=inclusive_start, start=start, exclusive_end=exclusive_end, end=end, app_id=app_id, device_id=device_id, topic=topic, page_limit=page_limit, page_sort=page_sort, page_next_token=page_next_token)
        print("The response of MessagesApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inclusive_start** | **datetime**|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **exclusive_end** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **app_id** | **str**| Filter returned messages by appId. Primarily used by Asset Tracker, AppId is taken from the \&quot;appId\&quot; property of the message body and is intended to represent the type of data being sent. This can be used to categorize your messages for easy filtering when using the same topic. | [optional] 
 **device_id** | **str**| A device Id to fetch messages for. Can be specified with appId or topic. | [optional] 
 **topic** | **str**| Fetch messages for a single topic. Can be specified with deviceId. | [optional] 
 **page_limit** | **int**|  | [optional] 
 **page_sort** | [**PageSort**](.md)|  | [optional] [default to desc]
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultDeviceMessage**](PaginatedResultDeviceMessage.md)

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

# **send_device_message**
> send_device_message(device_id, device_message_input)

SendDeviceMessage

Allows a user or [IP device](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Properties/Types.html) to
send a message that is subsequently published over an MQTT topic, on behalf of the
IP device whose deviceId is specified. The device ID for the message comes from the topic. For instance,
if the topic property on the request is `m/d/nrf-352656101081837/d2c/custom`, the device ID determined
for the message will be `'nrf-352656101081837'`.

For [dictionary based binary logs](https://docs.nordicsemi.com/bundle/ncs-latest/page/zephyr/services/logging/index.html#dictionary-based_logging) via the `d2c/bin` topic, the message must be base64 encoded.
For instance, for the device  `nrf-352656101081837` the request body would be:
```json
{
  "topic": "d/nrf-352656101081837/d2c/bin",
  "message": "blJGQwAAAAAd2qCkkAEAAAEAAABoZWxsbyB3b3JsZA=="
}
```

For more information, see
[Sending device messages](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/MessagesAndAlerts/DeviceMessages.html#sending-device-messages).

### Example

* Bearer Authentication (Simple Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_message_input import DeviceMessageInput
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
    api_instance = nrf_cloud_client.MessagesApi(api_client)
    device_id = 'device_id_example' # str | 
    device_message_input = nrf_cloud_client.DeviceMessageInput() # DeviceMessageInput | 

    try:
        # SendDeviceMessage
        api_instance.send_device_message(device_id, device_message_input)
    except Exception as e:
        print("Exception when calling MessagesApi->send_device_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **device_message_input** | [**DeviceMessageInput**](DeviceMessageInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

