# FileDownloadInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to download the file from. | 
**content_length** | **float** | Content length of the file in bytes. | 

## Example

```python
from nrf_cloud_client.models.file_download_info import FileDownloadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadInfo from a JSON string
file_download_info_instance = FileDownloadInfo.from_json(json)
# print the JSON string representation of the object
print(FileDownloadInfo.to_json())

# convert the object into a dict
file_download_info_dict = file_download_info_instance.to_dict()
# create an instance of FileDownloadInfo from a dict
file_download_info_from_dict = FileDownloadInfo.from_dict(file_download_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


