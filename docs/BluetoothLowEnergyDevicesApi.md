# nrf_cloud_client.BluetoothLowEnergyDevicesApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_peripheral**](BluetoothLowEnergyDevicesApi.md#add_peripheral) | **PUT** /devices/{gatewayId}/{peripheralId} | AddPeripheral
[**fetch_characteristic_descriptor_value**](BluetoothLowEnergyDevicesApi.md#fetch_characteristic_descriptor_value) | **GET** /devices/{deviceId}/characteristics/{characteristicId}/descriptors/{descriptorId} | FetchDescriptorValue
[**fetch_characteristic_value**](BluetoothLowEnergyDevicesApi.md#fetch_characteristic_value) | **GET** /devices/{deviceId}/characteristics/{characteristicId} | FetchCharacteristicValue
[**start_peripheral_discovery**](BluetoothLowEnergyDevicesApi.md#start_peripheral_discovery) | **POST** /devices/{gatewayId}/discover/{peripheralId} | StartPeripheralDiscovery
[**update_characteristic_descriptor_value**](BluetoothLowEnergyDevicesApi.md#update_characteristic_descriptor_value) | **PUT** /devices/{deviceId}/characteristics/{characteristicId}/descriptors/{descriptorId} | UpdateDescriptorValue
[**update_characteristic_value**](BluetoothLowEnergyDevicesApi.md#update_characteristic_value) | **PUT** /devices/{deviceId}/characteristics/{characteristicId} | UpdateCharacteristicValue


# **add_peripheral**
> add_peripheral(gateway_id, peripheral_id)

AddPeripheral

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy devices will be removed soon.</div>

Initiate connection of a peripheral to a gateway by adding to the gateway's
`desired.desiredConnections` array the peripheral id.

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
    api_instance = nrf_cloud_client.BluetoothLowEnergyDevicesApi(api_client)
    gateway_id = 'gateway_id_example' # str | 
    peripheral_id = 'peripheral_id_example' # str | 

    try:
        # AddPeripheral
        api_instance.add_peripheral(gateway_id, peripheral_id)
    except Exception as e:
        print("Exception when calling BluetoothLowEnergyDevicesApi->add_peripheral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**|  | 
 **peripheral_id** | **str**|  | 

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
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_characteristic_descriptor_value**
> List[float] fetch_characteristic_descriptor_value(device_id, characteristic_id, descriptor_id)

FetchDescriptorValue

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy devices will be removed soon.</div>

Fetch the latest characteristic descriptor value that is cached as part of the device state in our database. It may not fetch the latest characteristic descriptor value that is on the device (which can take a quite long to retrieve directly via a REST). Therefore, this value can be stale. If you want the latest it is best to first call the `StartPeripheralDiscovery` [endpoint](#operation/StartPeripheralDiscovery) to force a rediscovery of the BLE device state.

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
    api_instance = nrf_cloud_client.BluetoothLowEnergyDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    characteristic_id = 'characteristic_id_example' # str | 
    descriptor_id = 'descriptor_id_example' # str | 

    try:
        # FetchDescriptorValue
        api_response = api_instance.fetch_characteristic_descriptor_value(device_id, characteristic_id, descriptor_id)
        print("The response of BluetoothLowEnergyDevicesApi->fetch_characteristic_descriptor_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BluetoothLowEnergyDevicesApi->fetch_characteristic_descriptor_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **characteristic_id** | **str**|  | 
 **descriptor_id** | **str**|  | 

### Return type

**List[float]**

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

# **fetch_characteristic_value**
> List[float] fetch_characteristic_value(device_id, characteristic_id)

FetchCharacteristicValue

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy devices will be removed soon.</div>

Fetch the latest characteristic value that is cached as part of the device state in our database. It may not fetch the latest characteristic value that is on the device (which can take a quite long to retrieve directly via a REST). Therefore, this value can be stale. If you want the latest it is best to first call the `StartPeripheralDiscovery` [endpoint](#operation/StartPeripheralDiscovery) to force a rediscovery of the BLE device state.

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
    api_instance = nrf_cloud_client.BluetoothLowEnergyDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    characteristic_id = 'characteristic_id_example' # str | 

    try:
        # FetchCharacteristicValue
        api_response = api_instance.fetch_characteristic_value(device_id, characteristic_id)
        print("The response of BluetoothLowEnergyDevicesApi->fetch_characteristic_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BluetoothLowEnergyDevicesApi->fetch_characteristic_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **characteristic_id** | **str**|  | 

### Return type

**List[float]**

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

# **start_peripheral_discovery**
> start_peripheral_discovery(gateway_id, peripheral_id)

StartPeripheralDiscovery

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy devices will be removed soon.</div>

Initiate a discovery process for a BLE device. When discovery is complete (30-60 seconds), results will be stored
in our database and retrievable for the device via the `FetchDevice` [endpoint](#operation/FetchDevice).

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
    api_instance = nrf_cloud_client.BluetoothLowEnergyDevicesApi(api_client)
    gateway_id = 'gateway_id_example' # str | 
    peripheral_id = 'peripheral_id_example' # str | 

    try:
        # StartPeripheralDiscovery
        api_instance.start_peripheral_discovery(gateway_id, peripheral_id)
    except Exception as e:
        print("Exception when calling BluetoothLowEnergyDevicesApi->start_peripheral_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**|  | 
 **peripheral_id** | **str**|  | 

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

# **update_characteristic_descriptor_value**
> update_characteristic_descriptor_value(device_id, characteristic_id, descriptor_id, request_body)

UpdateDescriptorValue

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy devices will be removed soon.</div>

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
    api_instance = nrf_cloud_client.BluetoothLowEnergyDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    characteristic_id = 'characteristic_id_example' # str | 
    descriptor_id = 'descriptor_id_example' # str | 
    request_body = [3.4] # List[float] | 

    try:
        # UpdateDescriptorValue
        api_instance.update_characteristic_descriptor_value(device_id, characteristic_id, descriptor_id, request_body)
    except Exception as e:
        print("Exception when calling BluetoothLowEnergyDevicesApi->update_characteristic_descriptor_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **characteristic_id** | **str**|  | 
 **descriptor_id** | **str**|  | 
 **request_body** | [**List[float]**](float.md)|  | 

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

# **update_characteristic_value**
> update_characteristic_value(device_id, characteristic_id, request_body)

UpdateCharacteristicValue

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">Support for Bluetooth Low Energy devices will be removed soon.</div>

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
    api_instance = nrf_cloud_client.BluetoothLowEnergyDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    characteristic_id = 'characteristic_id_example' # str | 
    request_body = [3.4] # List[float] | 

    try:
        # UpdateCharacteristicValue
        api_instance.update_characteristic_value(device_id, characteristic_id, request_body)
    except Exception as e:
        print("Exception when calling BluetoothLowEnergyDevicesApi->update_characteristic_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **characteristic_id** | **str**|  | 
 **request_body** | [**List[float]**](float.md)|  | 

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

