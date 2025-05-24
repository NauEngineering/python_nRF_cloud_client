# PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**UsageMetricDate**](UsageMetricDate.md) |  | [optional] 
**service** | [**Service**](Service.md) |  | 
**service_type** | [**ServiceTypeValue**](ServiceTypeValue.md) |  | [optional] 
**source** | [**MetricSource**](MetricSource.md) |  | [optional] 
**sum** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id import PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId

# TODO update the JSON string below
json = "{}"
# create an instance of PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId from a JSON string
pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id_instance = PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId.from_json(json)
# print the JSON string representation of the object
print(PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId.to_json())

# convert the object into a dict
pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id_dict = pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id_instance.to_dict()
# create an instance of PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId from a dict
pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id_from_dict = PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId.from_dict(pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


