# nrf_cloud_client.AlertsApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_device_alert**](AlertsApi.md#archive_device_alert) | **PATCH** /alerts/{id}/archive | ArchiveDeviceAlert
[**list_device_alerts**](AlertsApi.md#list_device_alerts) | **GET** /alerts | ListDeviceAlerts
[**restore_device_alert**](AlertsApi.md#restore_device_alert) | **PATCH** /alerts/{id}/restore | RestoreDeviceAlert


# **archive_device_alert**
> ArchivedAlert archive_device_alert(id)

ArchiveDeviceAlert

Archives an Alert. For more information, see our [nRF Cloud documentation on device alerts](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/MessagesAndAlerts/AlertsAndLogs/AlertsOverview.html).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.archived_alert import ArchivedAlert
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
    api_instance = nrf_cloud_client.AlertsApi(api_client)
    id = 'id_example' # str | The unique identifier for the alert

    try:
        # ArchiveDeviceAlert
        api_response = api_instance.archive_device_alert(id)
        print("The response of AlertsApi->archive_device_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->archive_device_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the alert | 

### Return type

[**ArchivedAlert**](ArchivedAlert.md)

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

# **list_device_alerts**
> PaginatedResultDeviceAlert list_device_alerts(device_ids=device_ids, status=status, page_limit=page_limit, page_sort=page_sort, page_next_token=page_next_token)

ListDeviceAlerts

Fetch device alerts. For more information, see our [nRF Cloud documentation on device alerts](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/MessagesAndAlerts/AlertsAndLogs/AlertsOverview.html).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.alert_status import AlertStatus
from nrf_cloud_client.models.page_sort import PageSort
from nrf_cloud_client.models.paginated_result_device_alert import PaginatedResultDeviceAlert
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
    api_instance = nrf_cloud_client.AlertsApi(api_client)
    device_ids = ['device_ids_example'] # List[str] | Fetch alerts optionally by device ids. (optional)
    status = nrf_cloud_client.AlertStatus() # AlertStatus | Fetch alerts optionally by Status. By default, both `ACTIVE` and `ARCHIVED` alerts are returned. (optional)
    page_limit = 56 # int |  (optional)
    page_sort = desc # PageSort |  (optional) (default to desc)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListDeviceAlerts
        api_response = api_instance.list_device_alerts(device_ids=device_ids, status=status, page_limit=page_limit, page_sort=page_sort, page_next_token=page_next_token)
        print("The response of AlertsApi->list_device_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_device_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**List[str]**](str.md)| Fetch alerts optionally by device ids. | [optional] 
 **status** | [**AlertStatus**](.md)| Fetch alerts optionally by Status. By default, both &#x60;ACTIVE&#x60; and &#x60;ARCHIVED&#x60; alerts are returned. | [optional] 
 **page_limit** | **int**|  | [optional] 
 **page_sort** | [**PageSort**](.md)|  | [optional] [default to desc]
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultDeviceAlert**](PaginatedResultDeviceAlert.md)

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

# **restore_device_alert**
> ActiveAlert restore_device_alert(id)

RestoreDeviceAlert

Restore an archived Alert. For more information, see our [nRF Cloud documentation on device alerts](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/MessagesAndAlerts/AlertsAndLogs/AlertsOverview.html).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.active_alert import ActiveAlert
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
    api_instance = nrf_cloud_client.AlertsApi(api_client)
    id = 'id_example' # str | The unique identifier for the alert

    try:
        # RestoreDeviceAlert
        api_response = api_instance.restore_device_alert(id)
        print("The response of AlertsApi->restore_device_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->restore_device_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the alert | 

### Return type

[**ActiveAlert**](ActiveAlert.md)

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

