# CreateJobInputTagsBundleId

A unique id created by the server when the firmware was uploaded (concatenation of firmware type, random string, and firmware version).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from nrf_cloud_client.models.create_job_input_tags_bundle_id import CreateJobInputTagsBundleId

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobInputTagsBundleId from a JSON string
create_job_input_tags_bundle_id_instance = CreateJobInputTagsBundleId.from_json(json)
# print the JSON string representation of the object
print(CreateJobInputTagsBundleId.to_json())

# convert the object into a dict
create_job_input_tags_bundle_id_dict = create_job_input_tags_bundle_id_instance.to_dict()
# create an instance of CreateJobInputTagsBundleId from a dict
create_job_input_tags_bundle_id_from_dict = CreateJobInputTagsBundleId.from_dict(create_job_input_tags_bundle_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


