# ServiceUsageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**fota_job_executions** | **float** |  | 
**location_services** | [**PickRecordLocationServicesLocationServiceUsageExcludeKeyofRecordLocationServicesLocationServiceUsageGROUNDFIX**](PickRecordLocationServicesLocationServiceUsageExcludeKeyofRecordLocationServicesLocationServiceUsageGROUNDFIX.md) |  | 
**stored_device_messages** | **float** |  | 
**messages_routed** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.service_usage_summary import ServiceUsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUsageSummary from a JSON string
service_usage_summary_instance = ServiceUsageSummary.from_json(json)
# print the JSON string representation of the object
print(ServiceUsageSummary.to_json())

# convert the object into a dict
service_usage_summary_dict = service_usage_summary_instance.to_dict()
# create an instance of ServiceUsageSummary from a dict
service_usage_summary_from_dict = ServiceUsageSummary.from_dict(service_usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


