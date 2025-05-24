# nrf_cloud_client.MqttTeamDevicesApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mqtt_team_device**](MqttTeamDevicesApi.md#create_mqtt_team_device) | **POST** /devices/mqtt-team | CreateTeamDevice
[**delete_mqtt_team_device**](MqttTeamDevicesApi.md#delete_mqtt_team_device) | **DELETE** /devices/mqtt-team/{deviceId} | DeleteTeamDevice
[**get_mqtt_team_device_certificate**](MqttTeamDevicesApi.md#get_mqtt_team_device_certificate) | **GET** /devices/mqtt-team/{deviceId} | GetTeamDeviceCertificate
[**rotate_mqtt_team_device_certificate**](MqttTeamDevicesApi.md#rotate_mqtt_team_device_certificate) | **PATCH** /devices/mqtt-team/{deviceId} | RotateTeamDeviceCertificate


# **create_mqtt_team_device**
> DeviceCertificate create_mqtt_team_device()

CreateTeamDevice

Provision a device and attach an IoT policy with permissions that grant access to MQTT topics for any device in your team.
This type of device can be useful in apps that need an MQTT client to monitor the messages on other devices, or for debugging and testing purposes.
When a new team device (and subsequent certificate) is created, both the public AND private keys are returned.
If the private key is lost, the certificate should be rotated to obtain a new public/private key pair.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_certificate import DeviceCertificate
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
    api_instance = nrf_cloud_client.MqttTeamDevicesApi(api_client)

    try:
        # CreateTeamDevice
        api_response = api_instance.create_mqtt_team_device()
        print("The response of MqttTeamDevicesApi->create_mqtt_team_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MqttTeamDevicesApi->create_mqtt_team_device: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceCertificate**](DeviceCertificate.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mqtt_team_device**
> delete_mqtt_team_device(device_id)

DeleteTeamDevice

Delete a team device and its associated certificate.

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
    api_instance = nrf_cloud_client.MqttTeamDevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # DeleteTeamDevice
        api_instance.delete_mqtt_team_device(device_id)
    except Exception as e:
        print("Exception when calling MqttTeamDevicesApi->delete_mqtt_team_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

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

# **get_mqtt_team_device_certificate**
> DeviceCertificate get_mqtt_team_device_certificate(device_id)

GetTeamDeviceCertificate

Retrieve the team device certificate if it exists.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_certificate import DeviceCertificate
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
    api_instance = nrf_cloud_client.MqttTeamDevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # GetTeamDeviceCertificate
        api_response = api_instance.get_mqtt_team_device_certificate(device_id)
        print("The response of MqttTeamDevicesApi->get_mqtt_team_device_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MqttTeamDevicesApi->get_mqtt_team_device_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceCertificate**](DeviceCertificate.md)

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

# **rotate_mqtt_team_device_certificate**
> DeviceCertificate rotate_mqtt_team_device_certificate(device_id)

RotateTeamDeviceCertificate

Create and attach a new certificate for a team device. Overwrite any previously associated certificate.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_certificate import DeviceCertificate
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
    api_instance = nrf_cloud_client.MqttTeamDevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # RotateTeamDeviceCertificate
        api_response = api_instance.rotate_mqtt_team_device_certificate(device_id)
        print("The response of MqttTeamDevicesApi->rotate_mqtt_team_device_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MqttTeamDevicesApi->rotate_mqtt_team_device_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceCertificate**](DeviceCertificate.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

