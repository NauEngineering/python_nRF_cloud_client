# DeviceDocMetaArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**DeviceDocMetaArgsCreatedAt**](DeviceDocMetaArgsCreatedAt.md) |  | [optional] 
**updated_at** | [**DeviceDocMetaArgsCreatedAt**](DeviceDocMetaArgsCreatedAt.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.device_doc_meta_args import DeviceDocMetaArgs

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDocMetaArgs from a JSON string
device_doc_meta_args_instance = DeviceDocMetaArgs.from_json(json)
# print the JSON string representation of the object
print(DeviceDocMetaArgs.to_json())

# convert the object into a dict
device_doc_meta_args_dict = device_doc_meta_args_instance.to_dict()
# create an instance of DeviceDocMetaArgs from a dict
device_doc_meta_args_from_dict = DeviceDocMetaArgs.from_dict(device_doc_meta_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


