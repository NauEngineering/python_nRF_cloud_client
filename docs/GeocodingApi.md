# nrf_cloud_client.GeocodingApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_data_from_coordinates**](GeocodingApi.md#get_address_data_from_coordinates) | **GET** /location/geo | GetAddressDataFromCoordinates


# **get_address_data_from_coordinates**
> ReverseGeoResponse get_address_data_from_coordinates(lat, lon, x_custom_device_id=x_custom_device_id)

GetAddressDataFromCoordinates

Convert a set of WGS 84 coordinates into a physical address. Only country and state/province/region are guaranteed.
Higher accuracy properties (street number, street, etc) are provided when available.

A 404 status code (not found) will be returned if nRF Cloud cannot determine at least country and state/province/region for the provided
coordinates.

nRF Cloud returns the address data closest to the submitted coordinates. Coordinates from a higher-density urban areas generally
provide better results. Coordinates from rural areas may return address data further away from the submitted coordinates. The system
returns an uncertainty property, which is the distance in meters away from the submitted coordinates.

Coordinates obtained with a high-accuracy method (GNSS / Wi-Fi) will provide address data closer to the actual device location
than coordinates obtained with lower-accuracy methods like cellular.

```sh
curl --location --request GET "https://api.nrfcloud.com/v1/location/geo?lat=45.524098&lon=-122.688408" \
--header "Authorization: Bearer $JWT" \
--header "Content-Type: application/json"
```

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.reverse_geo_response import ReverseGeoResponse
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
    api_instance = nrf_cloud_client.GeocodingApi(api_client)
    lat = 3.4 # float | 
    lon = 3.4 # float | 
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetAddressDataFromCoordinates
        api_response = api_instance.get_address_data_from_coordinates(lat, lon, x_custom_device_id=x_custom_device_id)
        print("The response of GeocodingApi->get_address_data_from_coordinates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->get_address_data_from_coordinates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**|  | 
 **lon** | **float**|  | 
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

[**ReverseGeoResponse**](ReverseGeoResponse.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns address data for a set of WGS 84 coordinates. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

