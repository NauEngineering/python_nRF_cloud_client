# AccountInfoArgsTeam

Information about your team that owns the devices accessible by your API key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-defined friendly name of the team | [optional] 
**tenant_id** | **str** | The UUID of the team owning the device(s) | 

## Example

```python
from nrf_cloud_client.models.account_info_args_team import AccountInfoArgsTeam

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoArgsTeam from a JSON string
account_info_args_team_instance = AccountInfoArgsTeam.from_json(json)
# print the JSON string representation of the object
print(AccountInfoArgsTeam.to_json())

# convert the object into a dict
account_info_args_team_dict = account_info_args_team_instance.to_dict()
# create an instance of AccountInfoArgsTeam from a dict
account_info_args_team_from_dict = AccountInfoArgsTeam.from_dict(account_info_args_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


