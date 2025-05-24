# nrf_cloud_client.FOTAJobsApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_fota_job**](FOTAJobsApi.md#apply_fota_job) | **POST** /fota-jobs/{jobId}/apply | ApplyFOTAJob
[**cancel_fota_job**](FOTAJobsApi.md#cancel_fota_job) | **PUT** /fota-jobs/{jobId}/cancel | CancelFOTAJob
[**create_fota_job**](FOTAJobsApi.md#create_fota_job) | **POST** /fota-jobs | CreateFOTAJob
[**delete_fota_job**](FOTAJobsApi.md#delete_fota_job) | **DELETE** /fota-jobs/{jobId} | DeleteFOTAJob
[**fetch_fota_job**](FOTAJobsApi.md#fetch_fota_job) | **GET** /fota-jobs/{jobId} | FetchFOTAJob
[**list_fota_jobs**](FOTAJobsApi.md#list_fota_jobs) | **GET** /fota-jobs | ListFOTAJobs


# **apply_fota_job**
> apply_fota_job(job_id)

ApplyFOTAJob

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
    api_instance = nrf_cloud_client.FOTAJobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # ApplyFOTAJob
        api_instance.apply_fota_job(job_id)
    except Exception as e:
        print("Exception when calling FOTAJobsApi->apply_fota_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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

# **cancel_fota_job**
> cancel_fota_job(job_id, reason=reason)

CancelFOTAJob

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
    api_instance = nrf_cloud_client.FOTAJobsApi(api_client)
    job_id = 'job_id_example' # str | 
    reason = 'reason_example' # str |  (optional)

    try:
        # CancelFOTAJob
        api_instance.cancel_fota_job(job_id, reason=reason)
    except Exception as e:
        print("Exception when calling FOTAJobsApi->cancel_fota_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **reason** | **str**|  | [optional] 

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

# **create_fota_job**
> CreateFOTAJob201Response create_fota_job(create_job_input)

CreateFOTAJob

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.create_fota_job201_response import CreateFOTAJob201Response
from nrf_cloud_client.models.create_job_input import CreateJobInput
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
    api_instance = nrf_cloud_client.FOTAJobsApi(api_client)
    create_job_input = nrf_cloud_client.CreateJobInput() # CreateJobInput | 

    try:
        # CreateFOTAJob
        api_response = api_instance.create_fota_job(create_job_input)
        print("The response of FOTAJobsApi->create_fota_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobsApi->create_fota_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_input** | [**CreateJobInput**](CreateJobInput.md)|  | 

### Return type

[**CreateFOTAJob201Response**](CreateFOTAJob201Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fota_job**
> delete_fota_job(job_id)

DeleteFOTAJob

Deletes a fota job. Does not affect executions associated with this job.

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
    api_instance = nrf_cloud_client.FOTAJobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # DeleteFOTAJob
        api_instance.delete_fota_job(job_id)
    except Exception as e:
        print("Exception when calling FOTAJobsApi->delete_fota_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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

# **fetch_fota_job**
> FOTAV2Job fetch_fota_job(job_id)

FetchFOTAJob

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.fotav2_job import FOTAV2Job
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
    api_instance = nrf_cloud_client.FOTAJobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # FetchFOTAJob
        api_response = api_instance.fetch_fota_job(job_id)
        print("The response of FOTAJobsApi->fetch_fota_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobsApi->fetch_fota_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**FOTAV2Job**](FOTAV2Job.md)

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

# **list_fota_jobs**
> PaginatedResultFOTAV2JobOrFotaJobV2Plus list_fota_jobs(page_limit=page_limit, page_next_token=page_next_token)

ListFOTAJobs

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_fotav2_job_or_fota_job_v2_plus import PaginatedResultFOTAV2JobOrFotaJobV2Plus
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
    api_instance = nrf_cloud_client.FOTAJobsApi(api_client)
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListFOTAJobs
        api_response = api_instance.list_fota_jobs(page_limit=page_limit, page_next_token=page_next_token)
        print("The response of FOTAJobsApi->list_fota_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FOTAJobsApi->list_fota_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultFOTAV2JobOrFotaJobV2Plus**](PaginatedResultFOTAV2JobOrFotaJobV2Plus.md)

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

