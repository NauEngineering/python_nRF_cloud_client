# nrf_cloud_client.AnchorsApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_anchor**](AnchorsApi.md#create_anchor) | **POST** /location/anchors | CreateAnchor
[**delete_anchor**](AnchorsApi.md#delete_anchor) | **DELETE** /location/anchors/{macAddress} | DeleteAnchor
[**fetch_anchor**](AnchorsApi.md#fetch_anchor) | **GET** /location/anchors/{macAddress} | FetchAnchor
[**list_anchors**](AnchorsApi.md#list_anchors) | **GET** /location/anchors | ListAnchors
[**update_anchor**](AnchorsApi.md#update_anchor) | **PATCH** /location/anchors/{macAddress} | UpdateAnchor


# **create_anchor**
> create_anchor(anchor_input)

CreateAnchor

Create an anchor record. Please note that we standardize all mac addresses to use colons, even if they're submitted with dashes.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.anchor_input import AnchorInput
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
    api_instance = nrf_cloud_client.AnchorsApi(api_client)
    anchor_input = nrf_cloud_client.AnchorInput() # AnchorInput | 

    try:
        # CreateAnchor
        api_instance.create_anchor(anchor_input)
    except Exception as e:
        print("Exception when calling AnchorsApi->create_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor_input** | [**AnchorInput**](AnchorInput.md)|  | 

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

# **delete_anchor**
> delete_anchor(mac_address)

DeleteAnchor

Delete an anchor record.

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
    api_instance = nrf_cloud_client.AnchorsApi(api_client)
    mac_address = 'mac_address_example' # str | 

    try:
        # DeleteAnchor
        api_instance.delete_anchor(mac_address)
    except Exception as e:
        print("Exception when calling AnchorsApi->delete_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_address** | **str**|  | 

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

# **fetch_anchor**
> Anchor fetch_anchor(mac_address)

FetchAnchor

Get an anchor by mac address.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.anchor import Anchor
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
    api_instance = nrf_cloud_client.AnchorsApi(api_client)
    mac_address = 'mac_address_example' # str | 

    try:
        # FetchAnchor
        api_response = api_instance.fetch_anchor(mac_address)
        print("The response of AnchorsApi->fetch_anchor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorsApi->fetch_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_address** | **str**|  | 

### Return type

[**Anchor**](Anchor.md)

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

# **list_anchors**
> PaginatedResultAnchor list_anchors(page_next_token=page_next_token, page_limit=page_limit)

ListAnchors

Get all anchors for your account.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_anchor import PaginatedResultAnchor
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
    api_instance = nrf_cloud_client.AnchorsApi(api_client)
    page_next_token = 'page_next_token_example' # str |  (optional)
    page_limit = 10 # float |  (optional) (default to 10)

    try:
        # ListAnchors
        api_response = api_instance.list_anchors(page_next_token=page_next_token, page_limit=page_limit)
        print("The response of AnchorsApi->list_anchors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorsApi->list_anchors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_next_token** | **str**|  | [optional] 
 **page_limit** | **float**|  | [optional] [default to 10]

### Return type

[**PaginatedResultAnchor**](PaginatedResultAnchor.md)

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

# **update_anchor**
> update_anchor(mac_address, anchor_update_input)

UpdateAnchor

Update an anchor record. Please note that we standardize all mac addresses to use colons, even if they're submitted with dashes.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.anchor_update_input import AnchorUpdateInput
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
    api_instance = nrf_cloud_client.AnchorsApi(api_client)
    mac_address = 'mac_address_example' # str | 
    anchor_update_input = nrf_cloud_client.AnchorUpdateInput() # AnchorUpdateInput | 

    try:
        # UpdateAnchor
        api_instance.update_anchor(mac_address, anchor_update_input)
    except Exception as e:
        print("Exception when calling AnchorsApi->update_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_address** | **str**|  | 
 **anchor_update_input** | [**AnchorUpdateInput**](AnchorUpdateInput.md)|  | 

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

