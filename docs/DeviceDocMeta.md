# DeviceDocMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.device_doc_meta import DeviceDocMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDocMeta from a JSON string
device_doc_meta_instance = DeviceDocMeta.from_json(json)
# print the JSON string representation of the object
print(DeviceDocMeta.to_json())

# convert the object into a dict
device_doc_meta_dict = device_doc_meta_instance.to_dict()
# create an instance of DeviceDocMeta from a dict
device_doc_meta_from_dict = DeviceDocMeta.from_dict(device_doc_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


