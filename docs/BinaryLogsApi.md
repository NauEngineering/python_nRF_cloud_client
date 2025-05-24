# nrf_cloud_client.BinaryLogsApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_binary_logs_url**](BinaryLogsApi.md#fetch_binary_logs_url) | **GET** /binary-logs/url | FetchBinaryLogsUrl


# **fetch_binary_logs_url**
> FileDownloadInfo fetch_binary_logs_url(device_id, start=start, end=end)

FetchBinaryLogsUrl

Fetches the URL to a zip file containing one or more binary log files for the requested device and time range.
The returned URL can be used to download the zip file.

For more information, see the [nRF Cloud documentation on binary logs](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/MessagesAndAlerts/AlertsAndLogs/Logs.html#downloading-binary-logs-through-the-api).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.file_download_info import FileDownloadInfo
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
    api_instance = nrf_cloud_client.BinaryLogsApi(api_client)
    device_id = 'device_id_example' # str | 
    start = '2013-10-20T19:20:30+01:00' # datetime | By default, the start time for the range is 24 hours before the current time. The range between start and end cannot be greater than 24 hours. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | By default, the end time for the range is the current time. The range between start and end cannot be greater than 24 hours. (optional)

    try:
        # FetchBinaryLogsUrl
        api_response = api_instance.fetch_binary_logs_url(device_id, start=start, end=end)
        print("The response of BinaryLogsApi->fetch_binary_logs_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinaryLogsApi->fetch_binary_logs_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **start** | **datetime**| By default, the start time for the range is 24 hours before the current time. The range between start and end cannot be greater than 24 hours. | [optional] 
 **end** | **datetime**| By default, the end time for the range is the current time. The range between start and end cannot be greater than 24 hours. | [optional] 

### Return type

[**FileDownloadInfo**](FileDownloadInfo.md)

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

