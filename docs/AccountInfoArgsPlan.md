# AccountInfoArgsPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_month_costs** | [**List[PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType]**](PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.md) |  | [optional] 
**current_month_total_cost** | **float** |  | [optional] 
**name** | [**ExtractPlanTypesENTERPRISE**](ExtractPlanTypesENTERPRISE.md) |  | 
**limits** | [**ApiLimitsDocumentModel**](ApiLimitsDocumentModel.md) |  | 
**proxy_usage_declarations** | [**ProxyUsageDeclarations**](ProxyUsageDeclarations.md) |  | 
**service_keys** | [**List[ServiceKeyInfo]**](ServiceKeyInfo.md) |  | [optional] 
**overages** | [**Overages**](Overages.md) |  | 

## Example

```python
from nrf_cloud_client.models.account_info_args_plan import AccountInfoArgsPlan

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoArgsPlan from a JSON string
account_info_args_plan_instance = AccountInfoArgsPlan.from_json(json)
# print the JSON string representation of the object
print(AccountInfoArgsPlan.to_json())

# convert the object into a dict
account_info_args_plan_dict = account_info_args_plan_instance.to_dict()
# create an instance of AccountInfoArgsPlan from a dict
account_info_args_plan_from_dict = AccountInfoArgsPlan.from_dict(account_info_args_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


