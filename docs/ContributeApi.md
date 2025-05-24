# nrf_cloud_client.ContributeApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contribute_location_data**](ContributeApi.md#contribute_location_data) | **POST** /location/contribute | ContributeLocationData
[**delete_contribution**](ContributeApi.md#delete_contribution) | **DELETE** /location/contribute/{id} | DeleteContribution
[**get_contributions**](ContributeApi.md#get_contributions) | **GET** /location/contribute | GetContributions


# **contribute_location_data**
> ContributeLocationData200Response contribute_location_data(location_contribution)

ContributeLocationData

A contribution is the association of observed cell and Wi-Fi signals with a known geographic position. Contributions help improve
the quality of location services and are available immediately in subsequent requests for the contributing team. More details coming soon on the
<a href="https://docs.nordicsemi.com/bundle/nrf-cloud/page/LocationServices/Features.html" target="_blank">nRF Cloud Location Services Guide</a>.

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.contribute_location_data200_response import ContributeLocationData200Response
from nrf_cloud_client.models.location_contribution import LocationContribution
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

# Configure Bearer authorization: Service Evaluation Token
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
    api_instance = nrf_cloud_client.ContributeApi(api_client)
    location_contribution = nrf_cloud_client.LocationContribution() # LocationContribution | 

    try:
        # ContributeLocationData
        api_response = api_instance.contribute_location_data(location_contribution)
        print("The response of ContributeApi->contribute_location_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributeApi->contribute_location_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_contribution** | [**LocationContribution**](LocationContribution.md)|  | 

### Return type

[**ContributeLocationData200Response**](ContributeLocationData200Response.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the ID of the contribution. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contribution**
> delete_contribution(id)

DeleteContribution

Deletes a contribution

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

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

# Configure Bearer authorization: Service Evaluation Token
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
    api_instance = nrf_cloud_client.ContributeApi(api_client)
    id = 'id_example' # str | 

    try:
        # DeleteContribution
        api_instance.delete_contribution(id)
    except Exception as e:
        print("Exception when calling ContributeApi->delete_contribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contributions**
> PaginatedResultContributionItem get_contributions(page_sort=page_sort, page_limit=page_limit, page_next_token=page_next_token)

GetContributions

Gets contributions

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.page_sort import PageSort
from nrf_cloud_client.models.paginated_result_contribution_item import PaginatedResultContributionItem
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

# Configure Bearer authorization: Service Evaluation Token
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
    api_instance = nrf_cloud_client.ContributeApi(api_client)
    page_sort = desc # PageSort |  (optional) (default to desc)
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # GetContributions
        api_response = api_instance.get_contributions(page_sort=page_sort, page_limit=page_limit, page_next_token=page_next_token)
        print("The response of ContributeApi->get_contributions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributeApi->get_contributions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_sort** | [**PageSort**](.md)|  | [optional] [default to desc]
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultContributionItem**](PaginatedResultContributionItem.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

