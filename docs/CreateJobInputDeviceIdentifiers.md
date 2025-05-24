# CreateJobInputDeviceIdentifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | [**CreateJobInputTagsBundleId**](CreateJobInputTagsBundleId.md) |  | 
**auto_apply** | **bool** | If set to false the job will not be applied immediately, but instead will be left in the \&quot;CREATED\&quot; status. The job can later be applied using POST /fota-jobs/{jobId}/apply | [optional] [default to True]
**name** | **str** | Friendly name for this job | [optional] 
**description** | **str** | Short description for this job | [optional] 
**device_identifiers** | **List[str]** | A list of device identifiers assigned to this job. | 

## Example

```python
from nrf_cloud_client.models.create_job_input_device_identifiers import CreateJobInputDeviceIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobInputDeviceIdentifiers from a JSON string
create_job_input_device_identifiers_instance = CreateJobInputDeviceIdentifiers.from_json(json)
# print the JSON string representation of the object
print(CreateJobInputDeviceIdentifiers.to_json())

# convert the object into a dict
create_job_input_device_identifiers_dict = create_job_input_device_identifiers_instance.to_dict()
# create an instance of CreateJobInputDeviceIdentifiers from a dict
create_job_input_device_identifiers_from_dict = CreateJobInputDeviceIdentifiers.from_dict(create_job_input_device_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


