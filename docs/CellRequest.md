# CellRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lte** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**ltecatm** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**nbiot** | [**List[LteCell]**](LteCell.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.cell_request import CellRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CellRequest from a JSON string
cell_request_instance = CellRequest.from_json(json)
# print the JSON string representation of the object
print(CellRequest.to_json())

# convert the object into a dict
cell_request_dict = cell_request_instance.to_dict()
# create an instance of CellRequest from a dict
cell_request_from_dict = CellRequest.from_dict(cell_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


