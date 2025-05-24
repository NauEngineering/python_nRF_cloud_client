# Contribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell** | [**List[CellObservation]**](CellObservation.md) |  | [optional] 
**wifi** | [**List[AccessPointObservation]**](AccessPointObservation.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.contribution import Contribution

# TODO update the JSON string below
json = "{}"
# create an instance of Contribution from a JSON string
contribution_instance = Contribution.from_json(json)
# print the JSON string representation of the object
print(Contribution.to_json())

# convert the object into a dict
contribution_dict = contribution_instance.to_dict()
# create an instance of Contribution from a dict
contribution_from_dict = Contribution.from_dict(contribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


