# PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | [**PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageTypeServiceId**](PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageTypeServiceId.md) |  | 
**service_description** | **str** |  | 
**quantity** | **float** |  | 
**price** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type import PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType

# TODO update the JSON string below
json = "{}"
# create an instance of PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType from a JSON string
pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type_instance = PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.from_json(json)
# print the JSON string representation of the object
print(PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.to_json())

# convert the object into a dict
pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type_dict = pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type_instance.to_dict()
# create an instance of PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType from a dict
pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type_from_dict = PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType.from_dict(pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


