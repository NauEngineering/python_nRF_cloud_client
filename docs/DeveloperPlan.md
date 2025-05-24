# DeveloperPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_month_costs** | [**List[PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType]**](PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.md) |  | [optional] 
**current_month_total_cost** | **float** |  | [optional] 
**name** | [**ExtractPlanTypesDEVELOPER**](ExtractPlanTypesDEVELOPER.md) |  | 
**limits** | [**ApiLimitsDocumentModel**](ApiLimitsDocumentModel.md) |  | 

## Example

```python
from nrf_cloud_client.models.developer_plan import DeveloperPlan

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperPlan from a JSON string
developer_plan_instance = DeveloperPlan.from_json(json)
# print the JSON string representation of the object
print(DeveloperPlan.to_json())

# convert the object into a dict
developer_plan_dict = developer_plan_instance.to_dict()
# create an instance of DeveloperPlan from a dict
developer_plan_from_dict = DeveloperPlan.from_dict(developer_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


