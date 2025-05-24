# ServiceKeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**service** | [**ServiceKeyType**](ServiceKeyType.md) |  | 
**enabled** | **bool** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.service_key_info import ServiceKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceKeyInfo from a JSON string
service_key_info_instance = ServiceKeyInfo.from_json(json)
# print the JSON string representation of the object
print(ServiceKeyInfo.to_json())

# convert the object into a dict
service_key_info_dict = service_key_info_instance.to_dict()
# create an instance of ServiceKeyInfo from a dict
service_key_info_from_dict = ServiceKeyInfo.from_dict(service_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


