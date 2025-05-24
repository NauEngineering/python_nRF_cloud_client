# D2COverages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agps** | **float** |  | [optional] 
**pgps** | **float** |  | [optional] 
**scell** | **float** |  | [optional] 
**mcell** | **float** |  | [optional] 
**wifi** | **float** |  | [optional] 
**reverse_geo** | **float** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from nrf_cloud_client.models.d2_c_overages import D2COverages

# TODO update the JSON string below
json = "{}"
# create an instance of D2COverages from a JSON string
d2_c_overages_instance = D2COverages.from_json(json)
# print the JSON string representation of the object
print(D2COverages.to_json())

# convert the object into a dict
d2_c_overages_dict = d2_c_overages_instance.to_dict()
# create an instance of D2COverages from a dict
d2_c_overages_from_dict = D2COverages.from_dict(d2_c_overages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


