# nrf_cloud_client.SingleCellApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_single_cell_location**](SingleCellApi.md#get_single_cell_location) | **GET** /location/single-cell | GetSingleCellLocation


# **get_single_cell_location**
> GetSingleCellLocation200Response get_single_cell_location(mcc, mnc, tac, eci, rsrp=rsrp, format=format, x_custom_device_id=x_custom_device_id)

GetSingleCellLocation

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has been deprecated. Please use the <a href="#tag/Ground-Fix">ground fix endpoint</a> instead.</div>

Gets the lat, lon, and uncertainty values based on the id of the LTE cell passed.
Returns a binary payload or JSON, depending on the format argument. Binary by default. When returning binary, the by content-type response header is "application/octet-stream".
```sh
curl -G $API_HOST/v1/location/single-cell -d "mcc=244" -d "mnc=91" -d "tac=4099" -d "eci=36078631" -d "format=json" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json"
```

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.get_single_cell_location200_response import GetSingleCellLocation200Response
from nrf_cloud_client.models.single_cell_format import SingleCellFormat
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
    api_instance = nrf_cloud_client.SingleCellApi(api_client)
    mcc = 56 # int | 
    mnc = nrf_cloud_client.Mnc() # Mnc | 
    tac = 56 # int | 
    eci = 56 # int | 
    rsrp = 3.4 # float |  (optional)
    format = nrf_cloud_client.SingleCellFormat() # SingleCellFormat |  (optional)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetSingleCellLocation
        api_response = api_instance.get_single_cell_location(mcc, mnc, tac, eci, rsrp=rsrp, format=format, x_custom_device_id=x_custom_device_id)
        print("The response of SingleCellApi->get_single_cell_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SingleCellApi->get_single_cell_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcc** | **int**|  | 
 **mnc** | [**Mnc**](.md)|  | 
 **tac** | **int**|  | 
 **eci** | **int**|  | 
 **rsrp** | **float**|  | [optional] 
 **format** | [**SingleCellFormat**](.md)|  | [optional] 
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

[**GetSingleCellLocation200Response**](GetSingleCellLocation200Response.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains file-chunk or JSON response, depending on format param |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

