# nrf_cloud_client.AssistedGPSApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_assistance_data**](AssistedGPSApi.md#get_assistance_data) | **GET** /location/agps | GetAssistanceData
[**get_file_size**](AssistedGPSApi.md#get_file_size) | **HEAD** /location/agps | GetFileSize


# **get_assistance_data**
> bytearray get_assistance_data(request_type=request_type, custom_types=custom_types, types=types, mcc=mcc, mnc=mnc, tac=tac, eci=eci, rsrp=rsrp, filtered=filtered, mask=mask, range=range, x_custom_device_id=x_custom_device_id)

GetAssistanceData

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has been deprecated. Please use the <a href="#tag/GNSS/operation/GetAssistanceData">GNSS GetAssistanceData endpoint</a> instead.</div>

Provides assistance data to the device. Enables a faster time-to-first-fix (TTFF) for the GPS modem. Returns the modem
parameters for the nRF91 GPS modem in a chunk. The chunk size is determined by the request Range header. See `GetFileSize` [endpoint](#operation/GetFileSize) for details.

__Basic Request__:
```sh
curl -G $API_HOST/v1/location/agps -H "Authorization: Bearer $JWT" -H "Content-Type: application/octet-stream" -H "Range: bytes=0-2200" --output agps.bin
```

__Custom Request__:
```sh
curl -G "$API_HOST/v1/location/agps" -d "types=8" -d "mcc=244" -d "mnc=91" -d "tac=4099" -d "eci=36078631" -H "Authorization: Bearer $JWT" -H "Content-Type: application/octet-stream" -H "Range: bytes=0-2200" --output agps.bin
```

__Type definitions__:
- 1 = GPS UTC
- 2 = GPS Ephemerides
- 3 = GPS Almanac
- 4 = Klobuchar Ionospheric Correction
- 5 = Nequick Ionospheric Correction
- 6 = GPS Time of Week
- 7 = GPS System Clock
- 8 = Location (lat/lon of cell)
- 9 = GPS Integrity

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.nrf_gps_message_type import NrfGpsMessageType
from nrf_cloud_client.models.request_type import RequestType
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
    api_instance = nrf_cloud_client.AssistedGPSApi(api_client)
    request_type = nrf_cloud_client.RequestType() # RequestType |  (optional)
    custom_types = [nrf_cloud_client.NrfGpsMessageType()] # List[NrfGpsMessageType] | Deprecated in favor of the 'types' param. (optional)
    types = [nrf_cloud_client.NrfGpsMessageType()] # List[NrfGpsMessageType] | Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] (optional)
    mcc = 56 # int |  (optional)
    mnc = nrf_cloud_client.Mnc() # Mnc |  (optional)
    tac = 56 # int |  (optional)
    eci = 56 # int |  (optional)
    rsrp = 3.4 # float |  (optional)
    filtered = True # bool |  (optional)
    mask = 3.4 # float |  (optional)
    range = 'range_example' # str |  (optional)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetAssistanceData
        api_response = api_instance.get_assistance_data(request_type=request_type, custom_types=custom_types, types=types, mcc=mcc, mnc=mnc, tac=tac, eci=eci, rsrp=rsrp, filtered=filtered, mask=mask, range=range, x_custom_device_id=x_custom_device_id)
        print("The response of AssistedGPSApi->get_assistance_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistedGPSApi->get_assistance_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_type** | [**RequestType**](.md)|  | [optional] 
 **custom_types** | [**List[NrfGpsMessageType]**](NrfGpsMessageType.md)| Deprecated in favor of the &#39;types&#39; param. | [optional] 
 **types** | [**List[NrfGpsMessageType]**](NrfGpsMessageType.md)| Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] | [optional] 
 **mcc** | **int**|  | [optional] 
 **mnc** | [**Mnc**](.md)|  | [optional] 
 **tac** | **int**|  | [optional] 
 **eci** | **int**|  | [optional] 
 **rsrp** | **float**|  | [optional] 
 **filtered** | **bool**|  | [optional] 
 **mask** | **float**|  | [optional] 
 **range** | **str**|  | [optional] 
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**206** | Contains chunk of file defined by the Range header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_size**
> object get_file_size(request_type=request_type, custom_types=custom_types, types=types, mcc=mcc, mnc=mnc, tac=tac, eci=eci, rsrp=rsrp, filtered=filtered, mask=mask)

GetFileSize

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has been deprecated. Please use the <a href="#tag/GNSS/operation/GetAssistanceDataSize">GNSS GetFileSize endpoint</a> instead.</div>

This endpoint is for advanced use cases where you need to set the Range header to something other than the payload size.
Normally you will just set the Range header to the payload limit for your modem gets the payload size of the modem
parameters. This endpoint returns the totalBytes in the `Content-Length` response header, no body.
The `Content-Length` header in the response can be used in the `Range` header for a subsequent `GET` request (same query string, just
`GET` instead of `HEAD` + `Range` header).
```sh
curl -I "$API_HOST/v1/location/agps" -H "Authorization: Bearer $JWT"
```
__Type definitions__:
- 1 = GPS UTC
- 2 = GPS Ephemerides
- 3 = GPS Almanac
- 4 = Klobuchar Ionospheric Correction
- 5 = Nequick Ionospheric Correction
- 6 = GPS Time of Week
- 7 = GPS System Clock
- 8 = Location (lat/lon of cell)
- 9 = GPS Integrity

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.nrf_gps_message_type import NrfGpsMessageType
from nrf_cloud_client.models.request_type import RequestType
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
    api_instance = nrf_cloud_client.AssistedGPSApi(api_client)
    request_type = nrf_cloud_client.RequestType() # RequestType |  (optional)
    custom_types = [nrf_cloud_client.NrfGpsMessageType()] # List[NrfGpsMessageType] | Deprecated in favor of the 'types' param. (optional)
    types = [nrf_cloud_client.NrfGpsMessageType()] # List[NrfGpsMessageType] | Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] (optional)
    mcc = 56 # int |  (optional)
    mnc = nrf_cloud_client.Mnc() # Mnc |  (optional)
    tac = 56 # int |  (optional)
    eci = 56 # int |  (optional)
    rsrp = 3.4 # float |  (optional)
    filtered = True # bool |  (optional)
    mask = 3.4 # float |  (optional)

    try:
        # GetFileSize
        api_response = api_instance.get_file_size(request_type=request_type, custom_types=custom_types, types=types, mcc=mcc, mnc=mnc, tac=tac, eci=eci, rsrp=rsrp, filtered=filtered, mask=mask)
        print("The response of AssistedGPSApi->get_file_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistedGPSApi->get_file_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_type** | [**RequestType**](.md)|  | [optional] 
 **custom_types** | [**List[NrfGpsMessageType]**](NrfGpsMessageType.md)| Deprecated in favor of the &#39;types&#39; param. | [optional] 
 **types** | [**List[NrfGpsMessageType]**](NrfGpsMessageType.md)| Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] | [optional] 
 **mcc** | **int**|  | [optional] 
 **mnc** | [**Mnc**](.md)|  | [optional] 
 **tac** | **int**|  | [optional] 
 **eci** | **int**|  | [optional] 
 **rsrp** | **float**|  | [optional] 
 **filtered** | **bool**|  | [optional] 
 **mask** | **float**|  | [optional] 

### Return type

**object**

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Body is empty. Response \&quot;Content-Length\&quot; header contains the size of the file (bytes). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

