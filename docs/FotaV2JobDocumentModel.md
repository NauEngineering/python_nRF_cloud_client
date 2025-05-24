# FotaV2JobDocumentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firmware_type** | [**FirmwareTypes**](FirmwareTypes.md) |  | 
**file_size** | **float** |  | 
**host** | **str** |  | 
**path** | **str** |  | 
**version** | **str** |  | 
**bundle_id** | **str** | Unique bundle identifier | 

## Example

```python
from nrf_cloud_client.models.fota_v2_job_document_model import FotaV2JobDocumentModel

# TODO update the JSON string below
json = "{}"
# create an instance of FotaV2JobDocumentModel from a JSON string
fota_v2_job_document_model_instance = FotaV2JobDocumentModel.from_json(json)
# print the JSON string representation of the object
print(FotaV2JobDocumentModel.to_json())

# convert the object into a dict
fota_v2_job_document_model_dict = fota_v2_job_document_model_instance.to_dict()
# create an instance of FotaV2JobDocumentModel from a dict
fota_v2_job_document_model_from_dict = FotaV2JobDocumentModel.from_dict(fota_v2_job_document_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


