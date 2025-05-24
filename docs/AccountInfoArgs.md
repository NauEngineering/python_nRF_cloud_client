# AccountInfoArgs

Describes general info for this user in this team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mqtt_endpoint** | **str** | The MQTT endpoint to connect to | 
**mqtt_topic_prefix** | **str** | The global prefix for all topics | 
**team** | [**AccountInfoArgsTeam**](AccountInfoArgsTeam.md) |  | 
**role** | [**TenantUserRole**](TenantUserRole.md) |  | 
**user_id** | **str** | Universally unique identifier | 
**tags** | **List[str]** | Your assigned list of device tags (device groups in the nrfcloud.com UI). You can access devices that have any of these tags assigned, and devices that have no tags assigned. | [optional] 
**plan** | [**AccountInfoArgsPlan**](AccountInfoArgsPlan.md) |  | 

## Example

```python
from nrf_cloud_client.models.account_info_args import AccountInfoArgs

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoArgs from a JSON string
account_info_args_instance = AccountInfoArgs.from_json(json)
# print the JSON string representation of the object
print(AccountInfoArgs.to_json())

# convert the object into a dict
account_info_args_dict = account_info_args_instance.to_dict()
# create an instance of AccountInfoArgs from a dict
account_info_args_from_dict = AccountInfoArgs.from_dict(account_info_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


