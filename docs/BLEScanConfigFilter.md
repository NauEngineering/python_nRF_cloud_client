# BLEScanConfigFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rssi** | **float** | Lowest accepted RSSI value for scan report. &#x60;0&#x60; disables filter. | [optional] 
**name** | **str** | Match start of advertisement name. Case sensitive. | [optional] 

## Example

```python
from nrf_cloud_client.models.ble_scan_config_filter import BLEScanConfigFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BLEScanConfigFilter from a JSON string
ble_scan_config_filter_instance = BLEScanConfigFilter.from_json(json)
# print the JSON string representation of the object
print(BLEScanConfigFilter.to_json())

# convert the object into a dict
ble_scan_config_filter_dict = ble_scan_config_filter_instance.to_dict()
# create an instance of BLEScanConfigFilter from a dict
ble_scan_config_filter_from_dict = BLEScanConfigFilter.from_dict(ble_scan_config_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


