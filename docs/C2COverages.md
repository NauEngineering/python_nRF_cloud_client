# C2COverages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agps** | **float** |  | [optional] 
**pgps** | **float** |  | [optional] 
**reverse_geo** | **float** |  | [optional] 
**ground_fix** | **float** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from nrf_cloud_client.models.c2_c_overages import C2COverages

# TODO update the JSON string below
json = "{}"
# create an instance of C2COverages from a JSON string
c2_c_overages_instance = C2COverages.from_json(json)
# print the JSON string representation of the object
print(C2COverages.to_json())

# convert the object into a dict
c2_c_overages_dict = c2_c_overages_instance.to_dict()
# create an instance of C2COverages from a dict
c2_c_overages_from_dict = C2COverages.from_dict(c2_c_overages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


