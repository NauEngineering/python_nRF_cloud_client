# GetLocationFromCellsOrWifiNetworksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lte** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**ltecatm** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**nbiot** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**wifi** | [**WifiAccessPointsRequest**](WifiAccessPointsRequest.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.get_location_from_cells_or_wifi_networks_request import GetLocationFromCellsOrWifiNetworksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetLocationFromCellsOrWifiNetworksRequest from a JSON string
get_location_from_cells_or_wifi_networks_request_instance = GetLocationFromCellsOrWifiNetworksRequest.from_json(json)
# print the JSON string representation of the object
print(GetLocationFromCellsOrWifiNetworksRequest.to_json())

# convert the object into a dict
get_location_from_cells_or_wifi_networks_request_dict = get_location_from_cells_or_wifi_networks_request_instance.to_dict()
# create an instance of GetLocationFromCellsOrWifiNetworksRequest from a dict
get_location_from_cells_or_wifi_networks_request_from_dict = GetLocationFromCellsOrWifiNetworksRequest.from_dict(get_location_from_cells_or_wifi_networks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


