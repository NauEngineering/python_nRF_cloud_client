# ProOrHigherPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_month_costs** | [**List[PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType]**](PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.md) |  | [optional] 
**current_month_total_cost** | **float** |  | [optional] 
**name** | [**PickPlanTypesExcludeKeyofPlanTypesDEVELOPER**](PickPlanTypesExcludeKeyofPlanTypesDEVELOPER.md) |  | 
**proxy_usage_declarations** | [**ProxyUsageDeclarations**](ProxyUsageDeclarations.md) |  | 
**service_keys** | [**List[ServiceKeyInfo]**](ServiceKeyInfo.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.pro_or_higher_plan import ProOrHigherPlan

# TODO update the JSON string below
json = "{}"
# create an instance of ProOrHigherPlan from a JSON string
pro_or_higher_plan_instance = ProOrHigherPlan.from_json(json)
# print the JSON string representation of the object
print(ProOrHigherPlan.to_json())

# convert the object into a dict
pro_or_higher_plan_dict = pro_or_higher_plan_instance.to_dict()
# create an instance of ProOrHigherPlan from a dict
pro_or_higher_plan_from_dict = ProOrHigherPlan.from_dict(pro_or_higher_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


