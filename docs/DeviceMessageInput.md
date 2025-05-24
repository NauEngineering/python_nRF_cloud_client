# DeviceMessageInput

Device message input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | A string specifying an MQTT topic. | [optional] 
**message** | [**DeviceMessageInputMessage**](DeviceMessageInputMessage.md) |  | 

## Example

```python
from nrf_cloud_client.models.device_message_input import DeviceMessageInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMessageInput from a JSON string
device_message_input_instance = DeviceMessageInput.from_json(json)
# print the JSON string representation of the object
print(DeviceMessageInput.to_json())

# convert the object into a dict
device_message_input_dict = device_message_input_instance.to_dict()
# create an instance of DeviceMessageInput from a dict
device_message_input_from_dict = DeviceMessageInput.from_dict(device_message_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


