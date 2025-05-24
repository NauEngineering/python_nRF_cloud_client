# AnchorUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | [optional] 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | [optional] 
**name** | **str** | Limit 32 characters. Only numbers, letters, underscores, dashes, and spaces allowed. All other characters will be removed. | [optional] 

## Example

```python
from nrf_cloud_client.models.anchor_update_input import AnchorUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnchorUpdateInput from a JSON string
anchor_update_input_instance = AnchorUpdateInput.from_json(json)
# print the JSON string representation of the object
print(AnchorUpdateInput.to_json())

# convert the object into a dict
anchor_update_input_dict = anchor_update_input_instance.to_dict()
# create an instance of AnchorUpdateInput from a dict
anchor_update_input_from_dict = AnchorUpdateInput.from_dict(anchor_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


