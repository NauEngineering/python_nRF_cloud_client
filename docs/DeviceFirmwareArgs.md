# DeviceFirmwareArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports** | **List[str]** |  | [optional] 
**app** | [**DeviceFirmwareArgsApp**](DeviceFirmwareArgsApp.md) |  | [optional] 
**ble_support** | **bool** |  | [optional] 
**boot** | **str** |  | [optional] 
**modem** | **str** |  | [optional] 
**smp_device_app_ver** | **str** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.device_firmware_args import DeviceFirmwareArgs

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFirmwareArgs from a JSON string
device_firmware_args_instance = DeviceFirmwareArgs.from_json(json)
# print the JSON string representation of the object
print(DeviceFirmwareArgs.to_json())

# convert the object into a dict
device_firmware_args_dict = device_firmware_args_instance.to_dict()
# create an instance of DeviceFirmwareArgs from a dict
device_firmware_args_from_dict = DeviceFirmwareArgs.from_dict(device_firmware_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


