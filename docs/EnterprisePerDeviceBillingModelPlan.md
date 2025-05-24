# EnterprisePerDeviceBillingModelPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_month_costs** | [**List[PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType]**](PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.md) |  | [optional] 
**current_month_total_cost** | **float** |  | [optional] 
**name** | [**ExtractPlanTypesENTERPRISE**](ExtractPlanTypesENTERPRISE.md) |  | 
**proxy_usage_declarations** | [**ProxyUsageDeclarations**](ProxyUsageDeclarations.md) |  | 
**service_keys** | [**List[ServiceKeyInfo]**](ServiceKeyInfo.md) |  | [optional] 
**overages** | [**Overages**](Overages.md) |  | 

## Example

```python
from nrf_cloud_client.models.enterprise_per_device_billing_model_plan import EnterprisePerDeviceBillingModelPlan

# TODO update the JSON string below
json = "{}"
# create an instance of EnterprisePerDeviceBillingModelPlan from a JSON string
enterprise_per_device_billing_model_plan_instance = EnterprisePerDeviceBillingModelPlan.from_json(json)
# print the JSON string representation of the object
print(EnterprisePerDeviceBillingModelPlan.to_json())

# convert the object into a dict
enterprise_per_device_billing_model_plan_dict = enterprise_per_device_billing_model_plan_instance.to_dict()
# create an instance of EnterprisePerDeviceBillingModelPlan from a dict
enterprise_per_device_billing_model_plan_from_dict = EnterprisePerDeviceBillingModelPlan.from_dict(enterprise_per_device_billing_model_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


