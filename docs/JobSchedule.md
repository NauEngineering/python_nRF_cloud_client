# JobSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_job_at_epoch_ms** | **float** | Determine the date when the job should automatically start. Number of milliseconds for this date since the UNIX epoch. | [optional] 
**lock_target_list_at_epoch_ms** | **float** | Determine the date in which the target list should automatically be set to LOCKED. Number of milliseconds for this date since the UNIX epoch. | [optional] 

## Example

```python
from nrf_cloud_client.models.job_schedule import JobSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of JobSchedule from a JSON string
job_schedule_instance = JobSchedule.from_json(json)
# print the JSON string representation of the object
print(JobSchedule.to_json())

# convert the object into a dict
job_schedule_dict = job_schedule_instance.to_dict()
# create an instance of JobSchedule from a dict
job_schedule_from_dict = JobSchedule.from_dict(job_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


