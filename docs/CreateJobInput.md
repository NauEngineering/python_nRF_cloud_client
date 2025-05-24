# CreateJobInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | [**CreateJobInputTagsBundleId**](CreateJobInputTagsBundleId.md) |  | 
**auto_apply** | **bool** | If set to false the job will not be applied immediately, but instead will be left in the \&quot;CREATED\&quot; status. The job can later be applied using POST /fota-jobs/{jobId}/apply | [optional] [default to True]
**name** | **str** | Friendly name for this job | [optional] 
**description** | **str** | Short description for this job | [optional] 
**tags** | **List[str]** | A list of valid tags in which a device must contain one of for it to be eligible for this job. | 
**device_ids** | **List[str]** | List of valid device identifiers for this job. | 
**device_identifiers** | **List[str]** | A list of device identifiers assigned to this job. Deprecated. Use deviceIds instead. | 
**firmware_type** | **str** | Currently not supported. Firmware type a device must support for it to be eligible for this job. | [optional] 
**firmware_versions** | **List[str]** | Currently not supported. A list of firmware versions for the given firmware type that a device must have for it to be eligible for this job. | [optional] 
**schedule** | [**JobSchedule**](JobSchedule.md) |  | [optional] 
**target_list_type** | **str** | Currently not supported. Determine whether a target list is LOCKED or UNLOCKED. An UNLOCKED target list allows devices that are newly eligible for the job (based on target criteria) to receive an execution. A LOCKED target prevents devices that are newly eligible to receive an execution. | [optional] 

## Example

```python
from nrf_cloud_client.models.create_job_input import CreateJobInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobInput from a JSON string
create_job_input_instance = CreateJobInput.from_json(json)
# print the JSON string representation of the object
print(CreateJobInput.to_json())

# convert the object into a dict
create_job_input_dict = create_job_input_instance.to_dict()
# create an instance of CreateJobInput from a dict
create_job_input_from_dict = CreateJobInput.from_dict(create_job_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


