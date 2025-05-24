# LocationContribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**ObservingDevice**](ObservingDevice.md) |  | [optional] 
**contributions** | [**List[Contribution]**](Contribution.md) |  | 
**position** | [**PositionResponse**](PositionResponse.md) |  | 

## Example

```python
from nrf_cloud_client.models.location_contribution import LocationContribution

# TODO update the JSON string below
json = "{}"
# create an instance of LocationContribution from a JSON string
location_contribution_instance = LocationContribution.from_json(json)
# print the JSON string representation of the object
print(LocationContribution.to_json())

# convert the object into a dict
location_contribution_dict = location_contribution_instance.to_dict()
# create an instance of LocationContribution from a dict
location_contribution_from_dict = LocationContribution.from_dict(location_contribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


