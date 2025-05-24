# nrf_cloud_client.BulkOpsRequestsApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_bulk_ops_request**](BulkOpsRequestsApi.md#fetch_bulk_ops_request) | **GET** /bulk-ops-requests/{bulkOpsRequestId} | FetchBulkOpsRequest
[**list_bulk_ops_requests**](BulkOpsRequestsApi.md#list_bulk_ops_requests) | **GET** /bulk-ops-requests | ListBulkOpsRequests


# **fetch_bulk_ops_request**
> BulkOpsRequestDetails fetch_bulk_ops_request(bulk_ops_request_id)

FetchBulkOpsRequest

Fetch a bulk operations request.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.bulk_ops_request_details import BulkOpsRequestDetails
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
    api_instance = nrf_cloud_client.BulkOpsRequestsApi(api_client)
    bulk_ops_request_id = 'bulk_ops_request_id_example' # str | 

    try:
        # FetchBulkOpsRequest
        api_response = api_instance.fetch_bulk_ops_request(bulk_ops_request_id)
        print("The response of BulkOpsRequestsApi->fetch_bulk_ops_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOpsRequestsApi->fetch_bulk_ops_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_ops_request_id** | **str**|  | 

### Return type

[**BulkOpsRequestDetails**](BulkOpsRequestDetails.md)

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

# **list_bulk_ops_requests**
> PaginatedResultBulkOpsRequestDetails list_bulk_ops_requests(status=status, start_requested_at=start_requested_at, end_requested_at=end_requested_at, page_limit=page_limit, page_next_token=page_next_token)

ListBulkOpsRequests

Fetch a list of bulk operations requests.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.bulk_ops_request_status import BulkOpsRequestStatus
from nrf_cloud_client.models.paginated_result_bulk_ops_request_details import PaginatedResultBulkOpsRequestDetails
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
    api_instance = nrf_cloud_client.BulkOpsRequestsApi(api_client)
    status = nrf_cloud_client.BulkOpsRequestStatus() # BulkOpsRequestStatus |  (optional)
    start_requested_at = 'start_requested_at_example' # str |  (optional)
    end_requested_at = 'end_requested_at_example' # str |  (optional)
    page_limit = 10 # float |  (optional) (default to 10)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListBulkOpsRequests
        api_response = api_instance.list_bulk_ops_requests(status=status, start_requested_at=start_requested_at, end_requested_at=end_requested_at, page_limit=page_limit, page_next_token=page_next_token)
        print("The response of BulkOpsRequestsApi->list_bulk_ops_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOpsRequestsApi->list_bulk_ops_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**BulkOpsRequestStatus**](.md)|  | [optional] 
 **start_requested_at** | **str**|  | [optional] 
 **end_requested_at** | **str**|  | [optional] 
 **page_limit** | **float**|  | [optional] [default to 10]
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultBulkOpsRequestDetails**](PaginatedResultBulkOpsRequestDetails.md)

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

