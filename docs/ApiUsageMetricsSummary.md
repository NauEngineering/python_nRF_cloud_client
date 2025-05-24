# ApiUsageMetricsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_devices** | [**DeviceCountByType**](DeviceCountByType.md) |  | 
**services** | [**List[ServiceUsageSummary]**](ServiceUsageSummary.md) |  | 

## Example

```python
from nrf_cloud_client.models.api_usage_metrics_summary import ApiUsageMetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsageMetricsSummary from a JSON string
api_usage_metrics_summary_instance = ApiUsageMetricsSummary.from_json(json)
# print the JSON string representation of the object
print(ApiUsageMetricsSummary.to_json())

# convert the object into a dict
api_usage_metrics_summary_dict = api_usage_metrics_summary_instance.to_dict()
# create an instance of ApiUsageMetricsSummary from a dict
api_usage_metrics_summary_from_dict = ApiUsageMetricsSummary.from_dict(api_usage_metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


