# CreateJobInputIdOrIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | [**CreateJobInputTagsBundleId**](CreateJobInputTagsBundleId.md) |  | 
**auto_apply** | **bool** | If set to false the job will not be applied immediately, but instead will be left in the \&quot;CREATED\&quot; status. The job can later be applied using POST /fota-jobs/{jobId}/apply | [optional] [default to True]
**name** | **str** | Friendly name for this job | [optional] 
**description** | **str** | Short description for this job | [optional] 
**device_ids** | **List[str]** | A list of device identifiers assigned to this job. | 
**device_identifiers** | **List[str]** | A list of device identifiers assigned to this job. | 

## Example

```python
from nrf_cloud_client.models.create_job_input_id_or_identifier import CreateJobInputIdOrIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobInputIdOrIdentifier from a JSON string
create_job_input_id_or_identifier_instance = CreateJobInputIdOrIdentifier.from_json(json)
# print the JSON string representation of the object
print(CreateJobInputIdOrIdentifier.to_json())

# convert the object into a dict
create_job_input_id_or_identifier_dict = create_job_input_id_or_identifier_instance.to_dict()
# create an instance of CreateJobInputIdOrIdentifier from a dict
create_job_input_id_or_identifier_from_dict = CreateJobInputIdOrIdentifier.from_dict(create_job_input_id_or_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


