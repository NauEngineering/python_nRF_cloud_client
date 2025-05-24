# Overages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agps** | **float** |  | [optional] 
**pgps** | **float** |  | [optional] 
**reverse_geo** | **float** |  | [optional] 
**ground_fix** | **float** |  | [optional] 
**type** | **str** |  | 
**scell** | **float** |  | [optional] 
**mcell** | **float** |  | [optional] 
**wifi** | **float** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.overages import Overages

# TODO update the JSON string below
json = "{}"
# create an instance of Overages from a JSON string
overages_instance = Overages.from_json(json)
# print the JSON string representation of the object
print(Overages.to_json())

# convert the object into a dict
overages_dict = overages_instance.to_dict()
# create an instance of Overages from a dict
overages_from_dict = Overages.from_dict(overages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


