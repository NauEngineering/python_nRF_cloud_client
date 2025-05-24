# DeviceStateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reported** | **Dict[str, object]** |  | [optional] 
**desired** | **Dict[str, object]** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.device_state_input import DeviceStateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStateInput from a JSON string
device_state_input_instance = DeviceStateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceStateInput.to_json())

# convert the object into a dict
device_state_input_dict = device_state_input_instance.to_dict()
# create an instance of DeviceStateInput from a dict
device_state_input_from_dict = DeviceStateInput.from_dict(device_state_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


