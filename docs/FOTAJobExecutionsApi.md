# nrf_cloud_client.FOTAJobExecutionsApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_current_pending_fota_job_execution**](FOTAJobExecutionsApi.md#fetch_current_pending_fota_job_execution) | **GET** /fota-job-executions/{deviceId}/current | FetchCurrentPendingFOTAJobExecution
[**fetch_fota_job_execution**](FOTAJobExecutionsApi.md#fetch_fota_job_execution) | **GET** /fota-job-executions/{deviceId}/{jobId} | FetchFOTAJobExecution
[**list_fota_job_execution_statuses**](FOTAJobExecutionsApi.md#list_fota_job_execution_statuses) | **GET** /fota-job-execution-statuses/{jobId} | ListFOTAJobExecutionStatuses
[**list_fota_job_executions_for_device**](FOTAJobExecutionsApi.md#list_fota_job_executions_for_device) | **GET** /fota-job-executions/{deviceId} | ListFOTAJobExecutionsForDevice
[**update_fota_job_execution_status**](FOTAJobExecutionsApi.md#update_fota_job_execution_status) | **PATCH** /fota-job-executions/{deviceId}/{jobId} | UpdateFOTAJobExecutionStatus


# **fetch_current_pending_fota_job_execution**
> FOTAJobExecution fetch_current_pending_fota_job_execution(device_id, firmware_type=firmware_type)

FetchCurrentPendingFOTAJobExecution

Fetches the pending (QUEUED or IN_PROGRESS) job execution with the earliest createdAt date. This will allow
consistent FIFO (First In First Out) processing of incoming executions.

### Example

* Bearer Authentication (Simple Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.fota_job_execution import FOTAJobExecution
from nrf_cloud_client.models.firmware_types import FirmwareTypes
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
    api_instance = nrf_cloud_client.FOTAJobExecutionsApi(api_client)
    device_id = 'device_id_example' # str | 
    firmware_type = nrf_cloud_client.FirmwareTypes() # FirmwareTypes | Return only executions with the given firmware type (optional)

    try:
        # FetchCurrentPendingFOTAJobExecution
        api_response = api_instance.fetch_current_pending_fota_job_execution(device_id, firmware_type=firmware_type)
        print("The response of FOTAJobExecutionsApi->fetch_current_pending_fota_job_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobExecutionsApi->fetch_current_pending_fota_job_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **firmware_type** | [**FirmwareTypes**](.md)| Return only executions with the given firmware type | [optional] 

### Return type

[**FOTAJobExecution**](FOTAJobExecution.md)

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

# **fetch_fota_job_execution**
> FetchFOTAJobExecution200Response fetch_fota_job_execution(device_id, job_id)

FetchFOTAJobExecution

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.fetch_fota_job_execution200_response import FetchFOTAJobExecution200Response
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
    api_instance = nrf_cloud_client.FOTAJobExecutionsApi(api_client)
    device_id = 'device_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        # FetchFOTAJobExecution
        api_response = api_instance.fetch_fota_job_execution(device_id, job_id)
        print("The response of FOTAJobExecutionsApi->fetch_fota_job_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobExecutionsApi->fetch_fota_job_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

[**FetchFOTAJobExecution200Response**](FetchFOTAJobExecution200Response.md)

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

# **list_fota_job_execution_statuses**
> PaginatedResultFOTAJobExecutionState list_fota_job_execution_statuses(job_id, status=status, page_limit=page_limit, page_next_token=page_next_token)

ListFOTAJobExecutionStatuses

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.fota_v2_job_execution_events import FotaV2JobExecutionEvents
from nrf_cloud_client.models.paginated_result_fota_job_execution_state import PaginatedResultFOTAJobExecutionState
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
    api_instance = nrf_cloud_client.FOTAJobExecutionsApi(api_client)
    job_id = 'job_id_example' # str | 
    status = nrf_cloud_client.FotaV2JobExecutionEvents() # FotaV2JobExecutionEvents |  (optional)
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListFOTAJobExecutionStatuses
        api_response = api_instance.list_fota_job_execution_statuses(job_id, status=status, page_limit=page_limit, page_next_token=page_next_token)
        print("The response of FOTAJobExecutionsApi->list_fota_job_execution_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobExecutionsApi->list_fota_job_execution_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **status** | [**FotaV2JobExecutionEvents**](.md)|  | [optional] 
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultFOTAJobExecutionState**](PaginatedResultFOTAJobExecutionState.md)

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

# **list_fota_job_executions_for_device**
> PaginatedResultFOTAJobExecution list_fota_job_executions_for_device(device_id, page_limit=page_limit, page_next_token=page_next_token)

ListFOTAJobExecutionsForDevice

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_fota_job_execution import PaginatedResultFOTAJobExecution
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
    api_instance = nrf_cloud_client.FOTAJobExecutionsApi(api_client)
    device_id = 'device_id_example' # str | 
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListFOTAJobExecutionsForDevice
        api_response = api_instance.list_fota_job_executions_for_device(device_id, page_limit=page_limit, page_next_token=page_next_token)
        print("The response of FOTAJobExecutionsApi->list_fota_job_executions_for_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobExecutionsApi->list_fota_job_executions_for_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultFOTAJobExecution**](PaginatedResultFOTAJobExecution.md)

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

# **update_fota_job_execution_status**
> update_fota_job_execution_status(device_id, job_id, update_fota_job_execution_status_request)

UpdateFOTAJobExecutionStatus

### Example

* Bearer Authentication (Simple Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.update_fota_job_execution_status_request import UpdateFOTAJobExecutionStatusRequest
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
    api_instance = nrf_cloud_client.FOTAJobExecutionsApi(api_client)
    device_id = 'device_id_example' # str | 
    job_id = 'job_id_example' # str | 
    update_fota_job_execution_status_request = nrf_cloud_client.UpdateFOTAJobExecutionStatusRequest() # UpdateFOTAJobExecutionStatusRequest | 

    try:
        # UpdateFOTAJobExecutionStatus
        api_instance.update_fota_job_execution_status(device_id, job_id, update_fota_job_execution_status_request)
    except Exception as e:
        print("Exception when calling FOTAJobExecutionsApi->update_fota_job_execution_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **job_id** | **str**|  | 
 **update_fota_job_execution_status_request** | [**UpdateFOTAJobExecutionStatusRequest**](UpdateFOTAJobExecutionStatusRequest.md)|  | 

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
**202** | Updated FOTA job execution status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

