# CreateJobInputTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | [**CreateJobInputTagsBundleId**](CreateJobInputTagsBundleId.md) |  | 
**auto_apply** | **bool** | If set to false the job will not be applied immediately, but instead will be left in the \&quot;CREATED\&quot; status. The job can later be applied using POST /fota-jobs/{jobId}/apply | [optional] [default to True]
**name** | **str** | Friendly name for this job | [optional] 
**description** | **str** | Short description for this job | [optional] 
**tags** | **List[str]** | A list of tags to apply the device to | 

## Example

```python
from nrf_cloud_client.models.create_job_input_tags import CreateJobInputTags

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobInputTags from a JSON string
create_job_input_tags_instance = CreateJobInputTags.from_json(json)
# print the JSON string representation of the object
print(CreateJobInputTags.to_json())

# convert the object into a dict
create_job_input_tags_dict = create_job_input_tags_instance.to_dict()
# create an instance of CreateJobInputTags from a dict
create_job_input_tags_from_dict = CreateJobInputTags.from_dict(create_job_input_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


