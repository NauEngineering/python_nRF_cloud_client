# FetchFOTAJobExecution200ResponseAnyOfJobDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **object** |  | 
**host** | **object** |  | 
**version** | **object** |  | 
**bundle_id** | **str** |  | 
**file_size** | **object** |  | 
**firmware_type** | **object** |  | 

## Example

```python
from nrf_cloud_client.models.fetch_fota_job_execution200_response_any_of_job_document import FetchFOTAJobExecution200ResponseAnyOfJobDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FetchFOTAJobExecution200ResponseAnyOfJobDocument from a JSON string
fetch_fota_job_execution200_response_any_of_job_document_instance = FetchFOTAJobExecution200ResponseAnyOfJobDocument.from_json(json)
# print the JSON string representation of the object
print(FetchFOTAJobExecution200ResponseAnyOfJobDocument.to_json())

# convert the object into a dict
fetch_fota_job_execution200_response_any_of_job_document_dict = fetch_fota_job_execution200_response_any_of_job_document_instance.to_dict()
# create an instance of FetchFOTAJobExecution200ResponseAnyOfJobDocument from a dict
fetch_fota_job_execution200_response_any_of_job_document_from_dict = FetchFOTAJobExecution200ResponseAnyOfJobDocument.from_dict(fetch_fota_job_execution200_response_any_of_job_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


