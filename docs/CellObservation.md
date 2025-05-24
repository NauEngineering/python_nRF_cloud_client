# CellObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell** | [**LteCell**](LteCell.md) |  | 
**cell_type** | [**LteContribution**](LteContribution.md) |  | 
**observed_at** | **str** | ISO 8601 format. Example 2021-03-07T21:02:51.907Z | 

## Example

```python
from nrf_cloud_client.models.cell_observation import CellObservation

# TODO update the JSON string below
json = "{}"
# create an instance of CellObservation from a JSON string
cell_observation_instance = CellObservation.from_json(json)
# print the JSON string representation of the object
print(CellObservation.to_json())

# convert the object into a dict
cell_observation_dict = cell_observation_instance.to_dict()
# create an instance of CellObservation from a dict
cell_observation_from_dict = CellObservation.from_dict(cell_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


