# nrf_cloud_client.PredictedGPSApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_predicted_assistance_data**](PredictedGPSApi.md#get_predicted_assistance_data) | **GET** /location/pgps | GetPredictedAssistanceData


# **get_predicted_assistance_data**
> GetPredictedAssistanceData200Response get_predicted_assistance_data(prediction_count=prediction_count, prediction_interval_minutes=prediction_interval_minutes, start_gps_day=start_gps_day, start_gps_time_of_day_seconds=start_gps_time_of_day_seconds, x_custom_device_id=x_custom_device_id)

GetPredictedAssistanceData

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has been deprecated. Please use the <a href="#tag/GNSS/operation/GetPredictedAssistanceData">GNSS GetPredicitonData endpoint</a> instead.</div>

Generates up to two weeks of gps predictions. The predictions are used by the nRF91 GPS modem
to enable a faster time-to-first-fix (TTFF) and provide offline navigation when out of range of an LTE cell.

Returns a link for easy download of the predictions file.

__Basic Request__:
```sh
curl -G $API_HOST/v1/location/pgps -H "Authorization: Bearer $JWT" -H "Content-Type: application/json"
```
__Custom Request__:
```sh
curl -G $API_HOST/v1/location/pgps  -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d "predictionCount=42" -d "predictionIntervalMinutes=240" -d "startGpsDay=15131" -d "startGpsTimeOfDaySeconds=0"
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
    api_instance = nrf_cloud_client.PredictedGPSApi(api_client)
    prediction_count = 3.4 # float |  (optional)
    prediction_interval_minutes = 3.4 # float |  (optional)
    start_gps_day = 3.4 # float |  (optional)
    start_gps_time_of_day_seconds = 3.4 # float |  (optional)
    x_custom_device_id = 'x_custom_device_id_example' # str |  (optional)

    try:
        # GetPredictedAssistanceData
        api_response = api_instance.get_predicted_assistance_data(prediction_count=prediction_count, prediction_interval_minutes=prediction_interval_minutes, start_gps_day=start_gps_day, start_gps_time_of_day_seconds=start_gps_time_of_day_seconds, x_custom_device_id=x_custom_device_id)
        print("The response of PredictedGPSApi->get_predicted_assistance_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictedGPSApi->get_predicted_assistance_data: %s\n" % e)
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

