# BLEDeviceStateValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characteristics** | [**Dict[str, CharacteristicsValue]**](CharacteristicsValue.md) |  | 
**uuid** | **str** |  | 

## Example

```python
from nrf_cloud_client.models.ble_device_state_value import BLEDeviceStateValue

# TODO update the JSON string below
json = "{}"
# create an instance of BLEDeviceStateValue from a JSON string
ble_device_state_value_instance = BLEDeviceStateValue.from_json(json)
# print the JSON string representation of the object
print(BLEDeviceStateValue.to_json())

# convert the object into a dict
ble_device_state_value_dict = ble_device_state_value_instance.to_dict()
# create an instance of BLEDeviceStateValue from a dict
ble_device_state_value_from_dict = BLEDeviceStateValue.from_dict(ble_device_state_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


