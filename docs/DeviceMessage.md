# DeviceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The UUID of the team owning the device(s) | 
**topic** | **str** | A string specifying an MQTT topic. | 
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**received_at** | **datetime** |  | 
**message** | **object** | Construct a type with a set of properties K of type T | 

## Example

```python
from nrf_cloud_client.models.device_message import DeviceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMessage from a JSON string
device_message_instance = DeviceMessage.from_json(json)
# print the JSON string representation of the object
print(DeviceMessage.to_json())

# convert the object into a dict
device_message_dict = device_message_instance.to_dict()
# create an instance of DeviceMessage from a dict
device_message_from_dict = DeviceMessage.from_dict(device_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


