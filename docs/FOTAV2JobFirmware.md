# FOTAV2JobFirmware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | [**FOTAV2JobFirmwareBundleId**](FOTAV2JobFirmwareBundleId.md) |  | 
**host** | **str** |  | 
**file_size** | **float** |  | 
**firmware_type** | [**FirmwareTypes**](FirmwareTypes.md) |  | 
**version** | **str** |  | 
**uris** | **List[str]** |  | 

## Example

```python
from nrf_cloud_client.models.fotav2_job_firmware import FOTAV2JobFirmware

# TODO update the JSON string below
json = "{}"
# create an instance of FOTAV2JobFirmware from a JSON string
fotav2_job_firmware_instance = FOTAV2JobFirmware.from_json(json)
# print the JSON string representation of the object
print(FOTAV2JobFirmware.to_json())

# convert the object into a dict
fotav2_job_firmware_dict = fotav2_job_firmware_instance.to_dict()
# create an instance of FOTAV2JobFirmware from a dict
fotav2_job_firmware_from_dict = FOTAV2JobFirmware.from_dict(fotav2_job_firmware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


