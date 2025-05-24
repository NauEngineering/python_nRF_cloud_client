# nrf_cloud_client.WiFiLocationApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_from_wifi_networks**](WiFiLocationApi.md#get_location_from_wifi_networks) | **POST** /location/wifi | GetLocationFromWifiNetworks


# **get_location_from_wifi_networks**
> PositionResponseWithExtras get_location_from_wifi_networks(wifi_access_points_request, do_reply=do_reply, hi_conf=hi_conf, cont=cont, x_custom_device_id=x_custom_device_id)

GetLocationFromWifiNetworks

<div style="background-color: #fff3cd; color: #856404; text-align: center; border: 1px solid #ffeeba; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has an alternative. See the <a href="#tag/Ground-Fix">ground fix endpoint</a> for more details.</div>
Get location based on nearby Wi-Fi networks. At least two Access Points are required.

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.position_response_with_extras import PositionResponseWithExtras
from nrf_cloud_client.models.wifi_access_points_request import WifiAccessPointsRequest
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
    api_instance = nrf_cloud_client.WiFiLocationApi(api_client)
    wifi_access_points_request = nrf_cloud_client.WifiAccessPointsRequest() # WifiAccessPointsRequest | 
    do_reply = nrf_cloud_client.DoReplyFlag() # DoReplyFlag |  (optional)
    hi_conf = False # bool |  (optional) (default to False)
    cont = True # bool |  (optional) (default to True)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetLocationFromWifiNetworks
        api_response = api_instance.get_location_from_wifi_networks(wifi_access_points_request, do_reply=do_reply, hi_conf=hi_conf, cont=cont, x_custom_device_id=x_custom_device_id)
        print("The response of WiFiLocationApi->get_location_from_wifi_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WiFiLocationApi->get_location_from_wifi_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wifi_access_points_request** | [**WifiAccessPointsRequest**](WifiAccessPointsRequest.md)|  | 
 **do_reply** | [**DoReplyFlag**](.md)|  | [optional] 
 **hi_conf** | **bool**|  | [optional] [default to False]
 **cont** | **bool**|  | [optional] [default to True]
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

[**PositionResponseWithExtras**](PositionResponseWithExtras.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns lat/lon coordinates and uncertainty for a device using nearby Wi-Fi networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

