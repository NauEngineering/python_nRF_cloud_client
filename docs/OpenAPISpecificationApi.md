# nrf_cloud_client.OpenAPISpecificationApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spec**](OpenAPISpecificationApi.md#get_spec) | **GET** /openapi.json | FetchOpenApiSpec


# **get_spec**
> object get_spec()

FetchOpenApiSpec

Fetch the JSON document of this REST API, in OpenAPI format.
REST API tools such as Insomnia can import it into a request collection.

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
    api_instance = nrf_cloud_client.OpenAPISpecificationApi(api_client)

    try:
        # FetchOpenApiSpec
        api_response = api_instance.get_spec()
        print("The response of OpenAPISpecificationApi->get_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAPISpecificationApi->get_spec: %s\n" % e)
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
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

