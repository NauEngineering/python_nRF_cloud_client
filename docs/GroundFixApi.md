# nrf_cloud_client.GroundFixApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_from_cells_or_wifi_networks**](GroundFixApi.md#get_location_from_cells_or_wifi_networks) | **POST** /location/ground-fix | GetLocationFromCellsOrWifiNetworks


# **get_location_from_cells_or_wifi_networks**
> GroundFixResponseWithFulfillment get_location_from_cells_or_wifi_networks(get_location_from_cells_or_wifi_networks_request, do_reply=do_reply, fallback=fallback, hi_conf=hi_conf, dist=dist, cont=cont, alt=alt, x_custom_device_id=x_custom_device_id)

GetLocationFromCellsOrWifiNetworks

Gets the lat, lon, and uncertainty values for the LTE cell(s) or wifi access points passed. Wifi will be prioritized and fall back to LTE if unavailable.  At least two Access Points are required.

Return JSON payload.

__Basic Request__:
```sh
curl -X POST "$API_HOST/v1/location/ground-fix" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d "{\"lte\":[{\"mcc\": 244, \"mnc\": 91,\"tac\": 4099,\"eci\":36078631}], \"wifi\":[{\"macAddress\": \"00-18-39-59-8C-53\", \"ssid\": \"my-wifi-network\", \"signalStrength\": -42}, {\"macAddress\": \"00:21:55:61:F3:0A\", \"ssid\": \"my-other-wifi-network\", \"signalStrength\": -22}]}"
```

__Save device location and silence response__:
```sh
curl --verbose -X POST "$API_HOST/v1/location/ground-fix?doReply=false" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d "{\"lte\":[{\"mcc\": 244, \"mnc\": 91,\"tac\": 4099,\"eci\":36078631}], \"wifi\":[{\"macAddress\": \"00-18-39-59-8C-53\", \"ssid\": \"my-wifi-network\", \"signalStrength\": -42}, {\"macAddress\": \"00:21:55:61:F3:0A\", \"ssid\": \"my-other-wifi-network\", \"signalStrength\": -22}]}"
```

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.get_location_from_cells_or_wifi_networks_request import GetLocationFromCellsOrWifiNetworksRequest
from nrf_cloud_client.models.ground_fix_response_with_fulfillment import GroundFixResponseWithFulfillment
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
    api_instance = nrf_cloud_client.GroundFixApi(api_client)
    get_location_from_cells_or_wifi_networks_request = nrf_cloud_client.GetLocationFromCellsOrWifiNetworksRequest() # GetLocationFromCellsOrWifiNetworksRequest | 
    do_reply = nrf_cloud_client.DoReplyFlag() # DoReplyFlag |  (optional)
    fallback = True # bool |  (optional) (default to True)
    hi_conf = False # bool |  (optional) (default to False)
    dist = 3.4 # float |  (optional)
    cont = True # bool |  (optional) (default to True)
    alt = False # bool |  (optional) (default to False)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetLocationFromCellsOrWifiNetworks
        api_response = api_instance.get_location_from_cells_or_wifi_networks(get_location_from_cells_or_wifi_networks_request, do_reply=do_reply, fallback=fallback, hi_conf=hi_conf, dist=dist, cont=cont, alt=alt, x_custom_device_id=x_custom_device_id)
        print("The response of GroundFixApi->get_location_from_cells_or_wifi_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroundFixApi->get_location_from_cells_or_wifi_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_location_from_cells_or_wifi_networks_request** | [**GetLocationFromCellsOrWifiNetworksRequest**](GetLocationFromCellsOrWifiNetworksRequest.md)|  | 
 **do_reply** | [**DoReplyFlag**](.md)|  | [optional] 
 **fallback** | **bool**|  | [optional] [default to True]
 **hi_conf** | **bool**|  | [optional] [default to False]
 **dist** | **float**|  | [optional] 
 **cont** | **bool**|  | [optional] [default to True]
 **alt** | **bool**|  | [optional] [default to False]
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

[**GroundFixResponseWithFulfillment**](GroundFixResponseWithFulfillment.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns lat/lon coordinates and uncertainty for a device using cell or wifi data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

