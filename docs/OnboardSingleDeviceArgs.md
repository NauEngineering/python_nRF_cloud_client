# OnboardSingleDeviceArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** |  | 
**sub_type** | **str** | A custom string value to specify the type of thing (device) being provisioned on nRF Cloud. | [optional] 
**tags** | **List[str]** |  | [optional] 
**supported_firmware_types** | [**List[FirmwareTypes]**](FirmwareTypes.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.onboard_single_device_args import OnboardSingleDeviceArgs

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardSingleDeviceArgs from a JSON string
onboard_single_device_args_instance = OnboardSingleDeviceArgs.from_json(json)
# print the JSON string representation of the object
print(OnboardSingleDeviceArgs.to_json())

# convert the object into a dict
onboard_single_device_args_dict = onboard_single_device_args_instance.to_dict()
# create an instance of OnboardSingleDeviceArgs from a dict
onboard_single_device_args_from_dict = OnboardSingleDeviceArgs.from_dict(onboard_single_device_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


