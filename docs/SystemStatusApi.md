# nrf_cloud_client.SystemStatusApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_status**](SystemStatusApi.md#get_system_status) | **GET** /status | GetSystemStatus


# **get_system_status**
> object get_system_status()

GetSystemStatus

Get the status of the nRF Cloud system, returning a JSON object.
A "status" of "offline" is set when maintenance upgrades are in progress.
A "login" of "false" signifies that user logins to the nrfcloud.com portal have been temporarily disabled.

### Example


```python
import nrf_cloud_client
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)


# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.SystemStatusApi(api_client)

    try:
        # GetSystemStatus
        api_response = api_instance.get_system_status()
        print("The response of SystemStatusApi->get_system_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->get_system_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains system status information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

