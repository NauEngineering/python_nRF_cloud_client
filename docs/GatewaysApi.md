# nrf_cloud_client.GatewaysApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_scan_for_ble_devices**](GatewaysApi.md#start_scan_for_ble_devices) | **POST** /devices/{deviceId}/scan | StartScanForBLEDevices


# **start_scan_for_ble_devices**
> start_scan_for_ble_devices(device_id, ble_scan_config=ble_scan_config)

StartScanForBLEDevices

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy gateway devices will be removed soon.</div>

Initiate a gateway scan for BLE devices.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.ble_scan_config import BLEScanConfig
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
    api_instance = nrf_cloud_client.GatewaysApi(api_client)
    device_id = 'device_id_example' # str | 
    ble_scan_config = nrf_cloud_client.BLEScanConfig() # BLEScanConfig |  (optional)

    try:
        # StartScanForBLEDevices
        api_instance.start_scan_for_ble_devices(device_id, ble_scan_config=ble_scan_config)
    except Exception as e:
        print("Exception when calling GatewaysApi->start_scan_for_ble_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **ble_scan_config** | [**BLEScanConfig**](BLEScanConfig.md)|  | [optional] 

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

