# WifiAccessPointsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_points** | [**List[AccessPoint]**](AccessPoint.md) |  | 

## Example

```python
from nrf_cloud_client.models.wifi_access_points_request import WifiAccessPointsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WifiAccessPointsRequest from a JSON string
wifi_access_points_request_instance = WifiAccessPointsRequest.from_json(json)
# print the JSON string representation of the object
print(WifiAccessPointsRequest.to_json())

# convert the object into a dict
wifi_access_points_request_dict = wifi_access_points_request_instance.to_dict()
# create an instance of WifiAccessPointsRequest from a dict
wifi_access_points_request_from_dict = WifiAccessPointsRequest.from_dict(wifi_access_points_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


