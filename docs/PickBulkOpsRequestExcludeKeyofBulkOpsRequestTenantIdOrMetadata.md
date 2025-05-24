# PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_ops_request_id** | **str** | Universally Unique Lexicographically Sortable Identifier (using Crockford&#39;s alphabet). | 
**endpoint** | [**BulkOpsRequestEndpoint**](BulkOpsRequestEndpoint.md) |  | 
**status** | [**BulkOpsRequestStatus**](BulkOpsRequestStatus.md) |  | 
**requested_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | 
**completed_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | [optional] 

## Example

```python
from nrf_cloud_client.models.pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata import PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata from a JSON string
pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata_instance = PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata.from_json(json)
# print the JSON string representation of the object
print(PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata.to_json())

# convert the object into a dict
pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata_dict = pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata_instance.to_dict()
# create an instance of PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata from a dict
pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata_from_dict = PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata.from_dict(pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


