# FOTAV2JobExecutionStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_executions** | **float** |  | 
**executions** | **float** |  | 
**devices** | **float** |  | 
**timed_out** | **float** |  | 
**removed** | **float** |  | 
**downloading** | **float** |  | 
**in_progress** | **float** |  | 
**queued** | **float** |  | 
**rejected** | **float** |  | 
**failed** | **float** |  | 
**succeeded** | **float** |  | 
**cancelled** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.fotav2_job_execution_stats import FOTAV2JobExecutionStats

# TODO update the JSON string below
json = "{}"
# create an instance of FOTAV2JobExecutionStats from a JSON string
fotav2_job_execution_stats_instance = FOTAV2JobExecutionStats.from_json(json)
# print the JSON string representation of the object
print(FOTAV2JobExecutionStats.to_json())

# convert the object into a dict
fotav2_job_execution_stats_dict = fotav2_job_execution_stats_instance.to_dict()
# create an instance of FOTAV2JobExecutionStats from a dict
fotav2_job_execution_stats_from_dict = FOTAV2JobExecutionStats.from_dict(fotav2_job_execution_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


