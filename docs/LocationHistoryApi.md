# nrf_cloud_client.LocationHistoryApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_location_history**](LocationHistoryApi.md#delete_location_history) | **DELETE** /location/history/{deviceId}/{id} | DeleteLocationHistory
[**get_location_history**](LocationHistoryApi.md#get_location_history) | **GET** /location/history | GetLocationHistory


# **delete_location_history**
> delete_location_history(device_id, id)

DeleteLocationHistory

Delete a location history record.

### Example


```python
import nrf_cloud_client
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)


# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.LocationHistoryApi(api_client)
    device_id = 'device_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # DeleteLocationHistory
        api_instance.delete_location_history(device_id, id)
    except Exception as e:
        print("Exception when calling LocationHistoryApi->delete_location_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_history**
> PaginatedResultLocationTrackerItem get_location_history(device_id=device_id, latest=latest, page_sort=page_sort, start=start, end=end, page_limit=page_limit, page_next_token=page_next_token, device_identifier=device_identifier, inclusive_start=inclusive_start, inclusive_end=inclusive_end, tags=tags)

GetLocationHistory

Get location history for one, all, or a group of devices specified by tags parameter.

Notes:
- Location history data expires after ~6 months (27 weeks)
- The `serviceType` field is intentionally empty for location data before December 10th 2021

__Basic Request for device history__:
```sh
curl -G $API_HOST/v1/location/history -d "deviceId=$DEVICE_ID&start=2022-10-15T06:00:00.000Z&end=2022-10-16T18:30:00.000Z" -H "Authorization: Bearer $API_KEY"
```

__Paginated Request__:
```sh
export PAGE_NEXT_TOKEN=$(curl -G $API_HOST/v1/location/history -d "deviceId=$DEVICE_ID&start=2022-10-15T06:00:00.000Z&end=2022-10-16T18:30:00.000Z" -H "Authorization: Bearer $API_KEY" | jq .pageNextToken)

curl -G $API_HOST/v1/location/history -d "deviceId=$DEVICE_ID" --data-urlencode "pageNextToken=$PAGE_NEXT_TOKEN" -H "Authorization: Bearer $API_KEY"
```

__Request all devices location history__&dagger;:
```sh
curl -G $API_HOST/v1/location/history -H "Authorization: Bearer $API_KEY"
```

__Request all devices last known location__&dagger;:
```sh
curl -G $API_HOST/v1/location/history -d "latest=true" -H "Authorization: Bearer $API_KEY"
```

&dagger; Requires admin privileges

### Example


```python
import nrf_cloud_client
from nrf_cloud_client.models.page_sort import PageSort
from nrf_cloud_client.models.paginated_result_location_tracker_item import PaginatedResultLocationTrackerItem
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)


# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.LocationHistoryApi(api_client)
    device_id = 'device_id_example' # str | This is the canonical device id that is an optional parameter. Specify a device id to get its location history. If a device id is not provided, location history for all devices are returned. You must have admin privileges to perform this operation. (optional)
    latest = False # bool | Get the last known location for all devices or a single device (if deviceId is supplied). You must have admin privileges. (optional) (default to False)
    page_sort = desc # PageSort |  (optional) (default to desc)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)
    device_identifier = 'device_identifier_example' # str |  (optional)
    inclusive_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    inclusive_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    tags = ['tags_example'] # List[str] | If specified, only return location history for devices that have one of these Device Groups (tags). You must have admin privileges. (optional)

    try:
        # GetLocationHistory
        api_response = api_instance.get_location_history(device_id=device_id, latest=latest, page_sort=page_sort, start=start, end=end, page_limit=page_limit, page_next_token=page_next_token, device_identifier=device_identifier, inclusive_start=inclusive_start, inclusive_end=inclusive_end, tags=tags)
        print("The response of LocationHistoryApi->get_location_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationHistoryApi->get_location_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| This is the canonical device id that is an optional parameter. Specify a device id to get its location history. If a device id is not provided, location history for all devices are returned. You must have admin privileges to perform this operation. | [optional] 
 **latest** | **bool**| Get the last known location for all devices or a single device (if deviceId is supplied). You must have admin privileges. | [optional] [default to False]
 **page_sort** | [**PageSort**](.md)|  | [optional] [default to desc]
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 
 **device_identifier** | **str**|  | [optional] 
 **inclusive_start** | **datetime**|  | [optional] 
 **inclusive_end** | **datetime**|  | [optional] 
 **tags** | [**List[str]**](str.md)| If specified, only return location history for devices that have one of these Device Groups (tags). You must have admin privileges. | [optional] 

### Return type

[**PaginatedResultLocationTrackerItem**](PaginatedResultLocationTrackerItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains JSON response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

