# nrf_cloud_client.CellLocationApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_from_cells**](CellLocationApi.md#get_location_from_cells) | **POST** /location/cell | GetLocationFromCells


# **get_location_from_cells**
> CellResponseWithFulfillment get_location_from_cells(cell_request, do_reply=do_reply, fallback=fallback, hi_conf=hi_conf, cont=cont, x_custom_device_id=x_custom_device_id)

GetLocationFromCells

<div style="background-color: #fff3cd; color: #856404; text-align: center; border: 1px solid #ffeeba; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has an alternative. See the <a href="#tag/Ground-Fix">ground fix endpoint</a> for more details.</div>

Gets the lat, lon, and uncertainty values for the LTE cell(s) passed. If the optional `nmr` parameter is passed the endpoint operates in a "multi-cell" mode, using
more than one cell to determine a more accurate location.

__Basic Request__:
```sh
curl -X POST "$API_HOST/v1/location/cell" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d "{\"lte\":[{\"mcc\": 244, \"mnc\": 91,\"tac\": 4099,\"eci\":36078631}]}"
```

__Save device location and silence response__:
```sh
curl --verbose -X POST "$API_HOST/v1/location/cell?doReply=0" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d "{\"lte\":[{\"mcc\": 244, \"mnc\": 91,\"tac\": 4099,\"eci\":36078631}]}"
```

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.cell_request import CellRequest
from nrf_cloud_client.models.cell_response_with_fulfillment import CellResponseWithFulfillment
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
    api_instance = nrf_cloud_client.CellLocationApi(api_client)
    cell_request = nrf_cloud_client.CellRequest() # CellRequest | 
    do_reply = nrf_cloud_client.DoReplyFlag() # DoReplyFlag |  (optional)
    fallback = True # bool |  (optional) (default to True)
    hi_conf = False # bool |  (optional) (default to False)
    cont = True # bool |  (optional) (default to True)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetLocationFromCells
        api_response = api_instance.get_location_from_cells(cell_request, do_reply=do_reply, fallback=fallback, hi_conf=hi_conf, cont=cont, x_custom_device_id=x_custom_device_id)
        print("The response of CellLocationApi->get_location_from_cells:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CellLocationApi->get_location_from_cells: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_request** | [**CellRequest**](CellRequest.md)|  | 
 **do_reply** | [**DoReplyFlag**](.md)|  | [optional] 
 **fallback** | **bool**|  | [optional] [default to True]
 **hi_conf** | **bool**|  | [optional] [default to False]
 **cont** | **bool**|  | [optional] [default to True]
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

[**CellResponseWithFulfillment**](CellResponseWithFulfillment.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns lat/lon coordinates and uncertainty for a device using cell data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

