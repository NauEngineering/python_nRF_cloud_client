# nrf_cloud_client.GNSSApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_assistance_data**](GNSSApi.md#get_assistance_data) | **POST** /location/agnss | GetAssistanceData
[**get_assistance_data_size**](GNSSApi.md#get_assistance_data_size) | **HEAD** /location/agnss | GetAssistanceDataSize
[**get_predicted_assistance_data**](GNSSApi.md#get_predicted_assistance_data) | **GET** /location/pgnss | GetPredictionData
[**record_gnss_coordinates**](GNSSApi.md#record_gnss_coordinates) | **POST** /location/gnss | RecordGnssCoordinates


# **get_assistance_data**
> bytearray get_assistance_data(range=range, x_custom_device_id=x_custom_device_id, assistance_request=assistance_request)

GetAssistanceData

Provides assistance data to the device. Enables a faster time-to-first-fix (TTFF) for the GNSS modem. Returns the modem
parameters for the nRF GNSS modem in a chunk. The chunk size is determined by the request Range header.
See `GetAssistanceDataSize` [endpoint](#tag/GNSS/operation/GetAssistanceDataSize) for details.

__Basic Request__:
```sh
curl -X POST "$API_HOST/v1/location/agnss" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -H "Accept: application/octet-stream" -H "Range: bytes=0-2200" --output assistance.bin
```

__Custom Request__:
```sh
curl -X POST "$API_HOST/v1/location/agnss" -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -H "Accept: application/octet-stream" -H "Range: bytes=0-2200" --output assistance.bin -d "{\"types\": [8], \"mcc\": 244, \"mnc\": 91, \"tac\": 4099, \"eci\": 36078631}"
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
- 11 = QZSS Almanac
- 12 = QZSS Ephemerides
- 13 = QZSS Integrity

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.assistance_request import AssistanceRequest
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
    api_instance = nrf_cloud_client.GNSSApi(api_client)
    range = 'range_example' # str |  (optional)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)
    assistance_request = nrf_cloud_client.AssistanceRequest() # AssistanceRequest |  (optional)

    try:
        # GetAssistanceData
        api_response = api_instance.get_assistance_data(range=range, x_custom_device_id=x_custom_device_id, assistance_request=assistance_request)
        print("The response of GNSSApi->get_assistance_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GNSSApi->get_assistance_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**|  | [optional] 
 **x_custom_device_id** | **str**|  | [optional] 
 **assistance_request** | [**AssistanceRequest**](AssistanceRequest.md)|  | [optional] 

### Return type

**bytearray**

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**206** | Contains chunk of file defined by the Range header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assistance_data_size**
> object get_assistance_data_size(types=types, mcc=mcc, mnc=mnc, tac=tac, eci=eci, rsrp=rsrp, filtered=filtered, mask=mask)

GetAssistanceDataSize

This endpoint is for advanced use cases where you need to set the Range header to something other than the payload size.
Normally you will just set the Range header to the payload limit for your modem gets the payload size of the modem
parameters. This endpoint returns the totalBytes in the `Content-Length` response header, no body.
The `Content-Length` header in the response can be used in the `Range` header for a subsequent requests.

__Basic Request__:
```sh
curl -I $API_HOST/v1/location/agnss -H "Authorization: Bearer $JWT" -d "{\"types\": [8], \"mcc\": 244, \"mnc\": 91, \"tac\": 4099, \"eci\": 36078631}"
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
- 11 = QZSS Almanac
- 12 = QZSS Ephemerides
- 13 = QZSS Integrity

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.nrf_message_type import NrfMessageType
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
    api_instance = nrf_cloud_client.GNSSApi(api_client)
    types = [nrf_cloud_client.NrfMessageType()] # List[NrfMessageType] | Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] (optional)
    mcc = 56 # int |  (optional)
    mnc = nrf_cloud_client.Mnc() # Mnc |  (optional)
    tac = 56 # int |  (optional)
    eci = 56 # int |  (optional)
    rsrp = 3.4 # float |  (optional)
    filtered = True # bool |  (optional)
    mask = 3.4 # float |  (optional)

    try:
        # GetAssistanceDataSize
        api_response = api_instance.get_assistance_data_size(types=types, mcc=mcc, mnc=mnc, tac=tac, eci=eci, rsrp=rsrp, filtered=filtered, mask=mask)
        print("The response of GNSSApi->get_assistance_data_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GNSSApi->get_assistance_data_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**List[NrfMessageType]**](NrfMessageType.md)| Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] | [optional] 
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

# **get_predicted_assistance_data**
> GetPredictedAssistanceData200Response get_predicted_assistance_data(prediction_count=prediction_count, prediction_interval_minutes=prediction_interval_minutes, start_gps_day=start_gps_day, start_gps_time_of_day_seconds=start_gps_time_of_day_seconds, x_custom_device_id=x_custom_device_id)

GetPredictionData

Generates up to two weeks of GNSS predictions. The predictions are used by the nRF91 GNSS modem
to enable a faster time-to-first-fix (TTFF) and provide offline navigation when out of range of an LTE cell.

Returns a link for easy download of the predictions file.

__Basic Request__:
```sh
curl -G $API_HOST/v1/location/pgnss -H "Authorization: Bearer $JWT" -H "Content-Type: application/json"
```
__Custom Request__:
```sh
curl -G $API_HOST/v1/location/pgnss  -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d "predictionCount=42" -d "predictionIntervalMinutes=240" -d "startGpsDay=15131" -d "startGpsTimeOfDaySeconds=0"
```

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.get_predicted_assistance_data200_response import GetPredictedAssistanceData200Response
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
    api_instance = nrf_cloud_client.GNSSApi(api_client)
    prediction_count = 3.4 # float |  (optional)
    prediction_interval_minutes = 3.4 # float |  (optional)
    start_gps_day = 3.4 # float |  (optional)
    start_gps_time_of_day_seconds = 3.4 # float |  (optional)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetPredictionData
        api_response = api_instance.get_predicted_assistance_data(prediction_count=prediction_count, prediction_interval_minutes=prediction_interval_minutes, start_gps_day=start_gps_day, start_gps_time_of_day_seconds=start_gps_time_of_day_seconds, x_custom_device_id=x_custom_device_id)
        print("The response of GNSSApi->get_predicted_assistance_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GNSSApi->get_predicted_assistance_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prediction_count** | **float**|  | [optional] 
 **prediction_interval_minutes** | **float**|  | [optional] 
 **start_gps_day** | **float**|  | [optional] 
 **start_gps_time_of_day_seconds** | **float**|  | [optional] 
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

[**GetPredictedAssistanceData200Response**](GetPredictedAssistanceData200Response.md)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link to the P-GPS binary payload file for download. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_gnss_coordinates**
> record_gnss_coordinates(record_gnss_coordinates_request, x_custom_device_id=x_custom_device_id)

RecordGnssCoordinates

Report device coordinates, commonly obtained from the device's GNSS modem.

__Basic Request__:
```sh
curl --location --request POST "$API_HOST/v1/location/gnss" \
--header "Authorization: Bearer $JWT" \
--header "Content-Type: application/json" \
--data-raw "{\"lat\":$LAT, \"lon\":$LON, \"spd\":$SPD, \"acc\":$ACC, \"alt\":$ALT, \"hdg\":$HDG}"
```

### Example

* Bearer Authentication (Service Evaluation Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.record_gnss_coordinates_request import RecordGnssCoordinatesRequest
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
    api_instance = nrf_cloud_client.GNSSApi(api_client)
    record_gnss_coordinates_request = nrf_cloud_client.RecordGnssCoordinatesRequest() # RecordGnssCoordinatesRequest | 
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # RecordGnssCoordinates
        api_instance.record_gnss_coordinates(record_gnss_coordinates_request, x_custom_device_id=x_custom_device_id)
    except Exception as e:
        print("Exception when calling GNSSApi->record_gnss_coordinates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_gnss_coordinates_request** | [**RecordGnssCoordinatesRequest**](RecordGnssCoordinatesRequest.md)|  | 
 **x_custom_device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Service Evaluation Token](../README.md#Service Evaluation Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

