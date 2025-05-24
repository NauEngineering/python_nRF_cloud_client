# ContributionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier | 
**contributions** | [**List[Contribution]**](Contribution.md) |  | 
**device** | [**ObservingDevice**](ObservingDevice.md) |  | 
**position** | [**PositionResponse**](PositionResponse.md) |  | 
**created_at** | **str** |  | 

## Example

```python
from nrf_cloud_client.models.contribution_item import ContributionItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContributionItem from a JSON string
contribution_item_instance = ContributionItem.from_json(json)
# print the JSON string representation of the object
print(ContributionItem.to_json())

# convert the object into a dict
contribution_item_dict = contribution_item_instance.to_dict()
# create an instance of ContributionItem from a dict
contribution_item_from_dict = ContributionItem.from_dict(contribution_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


