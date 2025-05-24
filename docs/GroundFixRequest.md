# GroundFixRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lte** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**ltecatm** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**nbiot** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**wifi** | [**List[AccessPoint]**](AccessPoint.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.ground_fix_request import GroundFixRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroundFixRequest from a JSON string
ground_fix_request_instance = GroundFixRequest.from_json(json)
# print the JSON string representation of the object
print(GroundFixRequest.to_json())

# convert the object into a dict
ground_fix_request_dict = ground_fix_request_instance.to_dict()
# create an instance of GroundFixRequest from a dict
ground_fix_request_from_dict = GroundFixRequest.from_dict(ground_fix_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


