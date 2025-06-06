# coding: utf-8

# flake8: noqa

"""
    nRF Cloud REST API

    # Overview   The [nRF Cloud REST API](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/RESTOverview.html)   allows you to programmatically interact with, and retrieve historical information generated by, any device that you have   connected to <a href='https://nrfcloud.com'>nRFCloud.com</a>. This includes both IP-based devices–that is, devices that have an IP address and can talk directly to our   IoT platform–and Bluetooth Low Energy (BLE) devices, which require the use of an IP-based device (a gateway).  The REST API documentation is a supplement to the <a href='https://docs.nordicsemi.com/bundle/nrf-cloud/page/index.html'>main nRF Cloud documentation</a>.  [DevZone](https://devzone.nordicsemi.com) is Nordic Semiconductor's official tech support site and community. Get help from a dedicated tech support team and more than 25,000 other community members.  If you are encountering unexpected behavior or errors, check the current [status](https://status.nrfcloud.com) of nRF Cloud.  # Error Codes Some of the endpoints return specific error codes (called 'nRF Codes'), which can be found in this table.   <table>       <thead>       <tr>           <th style='width:10%'>nRF&nbsp;Code</th>           <th style='width:20%'>Error</th>           <th style='width:35%'>Reason</th>           <th style='width:35%'>Solution</th>       </tr>       </thead>       <tbody>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40000'>40000</div>           </td>           <td valign='top'>Bad request error.</td>           <td valign='top'>This error could mean many things. Most of the time it means something is not as expected               on the cloud like a file was missing or an internal service failed.           </td>           <td valign='top'>Alert Nordic support by filing a ticket on <a href='https://devzone.nordicsemi.com/'                                                                           target='_blank'>DevZone</a>.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40001'>40001</div>           </td>           <td valign='top'>Device does not have a valid device certificate for associating (adding) it to your               account.           </td>           <td valign='top'>Your nRF9160 DK device or Thingy:91 device does not have a 'just-in-time provisioning' (JITP) certificate, or               the certificate has been corrupted.           </td>           <td valign='top'>Refer to the <a                   href='https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/working_with_nrf/nrf91/nrf9160_gs.html'>               nRF9160 DK Getting Started Guide</a> or <a                   href='https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/working_with_nrf/nrf91/thingy91_gsg.html'>               Thingy:91 Getting Started Guide</a> for information on upgrading your device certificate.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40002'>40002</div>           </td>           <td valign='top'>Device cannot be dissociated (removed from your account).</td>           <td valign='top'>The nRF9160 DK or Thingy:91 you are trying to dissociate was added to your account using the legacy               pairing mechanism (button and switch pattern) instead of the <code>AssociateDevice</code> <a                       href='#operation/AssociateDevice'>endpoint</a>.           </td>           <td valign='top'>Delete the device from your account using either the <code>Configure</code> &gt; <code>Delete               Device</code> menu item on nrfcloud.com or the <code>DeleteDevice</code> <a                   href='#operation/DeleteDevice'>endpoint</a>. If you want to re-add this device to your account you               will first have to flash a new device certificate and upgrade the firmware. Refer to the <a                   href='https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/working_with_nrf/nrf91/nrf9160_gs.html'>               nRF9160 DK Getting Started Guide</a> or <a                   href='https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/working_with_nrf/nrf91/thingy91_gsg.html'>               Thingy:91 Getting Started Guide</a> for information on how to do this.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40005'>40005</div>           </td>           <td valign='top'>Usage limit exceeded.</td>           <td valign='top'>The API request exceeds one of the monthly usage limits defined on the               <a href='https://nrfcloud.com/#/pricing'>Pricing page</a> for users on the free Developer plan.           </td>           <td valign='top'>Wait until the beginning of the next month to continue your usage on the Developer               plan, or upgrade to the Pro or Enterprise plan.               See <a href='https://docs.nordicsemi.com/bundle/nrf-cloud/page/AccountAndTeamManagement/Plans/PlanOverview.html'>               nRF Cloud plans</a> to learn about the available plans, how to view your plan details and usage,               and how to upgrade your plan.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40100'>40100</div>           </td>           <td valign='top'>Access denied error.</td>           <td valign='top'>The user making the request does not have access to the requested resource (device, SIM,               invitation, etc.).           </td>           <td valign='top'>Confirm your authorization is correct. Refer to the endpoint's documentation to               determine if your request requires a Simple Token (API Key) or a JSON Web Token (JWT).               Some endpoints accept either.</td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40101'>40101</div>           </td>           <td valign='top'>Device is already associated with another account.</td>           <td valign='top'>Another user has already added this device to their account.</td>           <td valign='top'>If you know the other account owner you can request that they dissociate the device so that               you can add it to your account. Otherwise, this operation is not allowed.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40102'>40102</div>           </td>           <td valign='top'>The ownership code is invalid for this device.</td>           <td valign='top'>You entered the wrong ownership code (PIN or HWID) that is printed on the Nordic               Semiconductor product label, or which you submitted when creating a new device certificate.           </td>           <td valign='top'>Verify the PIN or HWID and enter it correctly.</td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40103'>40103</div>           </td>           <td valign='top'>This device is not associated with your account.</td>           <td valign='top'>The device you want to dissociate (remove from your account) is not found in your               account.           </td>           <td valign='top'>None. You are not allowed to do this.</td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40410'>40410</div>           </td>           <td valign='top'>Entity not found.           </td>           <td valign='top'>This error can be thrown for a variety of reasons, indicating that the entity could not be found by its ID. The entity could be a device, a certificate, or an API key, for example.           </td>           <td valign='top'>Refer to the associated message for details. For devices, confirm the device id you entered matches your existing device ID and that the device has not been deleted.               You can confirm using the <a href=\"/v1#operation/ListDevices\">ListDevices endpoint</a>.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40411'>40411</div>           </td>           <td valign='top'>A Nordic Semiconductor product with this device id and ownership code could not be found.           </td>           <td valign='top'>The device id you entered matches the format for a Nordic Semiconductor product, but the               device id and/or ownership code cannot be found in our system.           </td>           <td valign='top'>Compare the values you entered with what is printed on your product's label (for devices               with <code>IMEI</code> printed on the label, the device id will be <code>nrf-[IMEI]</code>, e.g., <code>nrf-123456789012345</code>).               If you submitted the correct values, please contact Nordic Semiconductor Tech Support for further               assistance.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40412'>40412</div>           </td>           <td valign='top'>No device found for this id. The device has not yet been provisioned.</td>           <td valign='top'>The device cannot be found in the nRF Cloud IoT device registry. The most likely reason               is that the device has not established an initial communication with the nRF Cloud MQTT broker, which               creates a new entry in the registry. Possible causes:<br><br>               <ol>                   <li>You entered the device id and/or ownership code (PIN or HWID) incorrectly.</li>                   <li>The device has not yet achieved an LTE connection, so it cannot contact nRF Cloud.</li>                   <li>The device has not completed the initial MQTT handshaking with nRF Cloud. Some hardware devices                       may indicate this completion using LED patterns.</li>                   <li>Corrupt modem firmware.</li>                   <li>Corrupt, wrongly flashed, or illegitimate device certificates.</li>                   <li>Poor LTE connection.</li>               </ol>           </td>           <td valign='top'>Solutions that match the possible reasons are listed here. For Nordic Semiconductor products,               refer to the <a href='https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/gsg_guides.html'>               Getting Started Guide</a> for your device.<br><br>               <ol>                   <li>Verify the values and try again. For Nordic Semiconductor products, please see the solution for                       nRF Code 40411, above.</li>                   <li>Ensure that the device's SIM card or eSIM is activated and functioning. If using an iBasis                       SIM card that is packaged with a Nordic Semiconductor product such as a Development                       Kit, activate the card on nrfcloud.com and then (re-)boot the device to connect.</li>                   <li>Check the LED status indicators to ensure the device indicates it has connected.</li>                   <li>(Re-)flash the latest modem firmware.</li>                   <li>Flash new device certificates obtained from the <code>CreateDeviceCertificate</code> <a                           href='#operation/CreateDeviceCertificate'> endpoint</a>.</li>                   <li>Move to a location with a better LTE connection.</li>               </ol>           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40413'>40413</div>           </td>           <td valign='top'>No device found for this id.</td>           <td valign='top'>You are trying to dissociate a device that is not found in your account (wrong device id),               or you are submitting the device's friendly name, not the id.           </td>           <td valign='top'>Verify you are passing the correct device id (not the friendly name you may have given               it).           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40414'>40414</div>           </td>           <td valign='top'>No device found for this id.</td>           <td valign='top'>You are trying to delete a device that was not found in your account or in the IoT registry               (i.e., provisioned, but not yet added to your account).           </td>           <td valign='top'><em>This may not be an error</em>, because the device may already be deleted. Verify you entered               the correct device id and ownership code (PIN or HWID on the label). For Nordic Semiconductor products,               see the solution for nRF Code 40411, above.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40420'>40420</div>           </td>           <td valign='top'>Resource not found.           </td>           <td valign='top'>This error can be thrown for a variety of reasons, indicating that a resource could not be found by its ID. The resource could be a device, a certificate, or an API key, for example.           </td>           <td valign='top'>Refer to the associated message for details. For devices, confirm the device id you entered matches your existing device ID and that the device has not been deleted.               You can confirm using the <a href=\"/v1#operation/ListDevices\">ListDevices endpoint</a>.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/40499'>40499</div>           </td>           <td valign='top'>Not found, but no error.</td>           <td valign='top'>The requested item(s) do not exist, but there is no error.               For some requests, if the list to be returned is empty, this code and an explanatory message is               returned instead of an empty list.           </td>           <td valign='top'>No action is necessary.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/41600'>41600</div>           </td>           <td valign='top'>Range not satisfiable.</td>           <td valign='top'>You are calling an endpoint that uses the Range header and the byte range does not exist in               the target file or the range header itself is malformed.           </td>           <td valign='top'>Check the expected file size for the target file and ensure the range requested exists.               Refer to the <a href='https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range' target='_blank'>range                   header docs</a> for more information.           </td>       </tr>       <tr>           <td valign='top'>               <div data-section-id='section/Error-Codes/42200'>42200</div>           </td>           <td valign='top'>Validation failed.</td>           <td valign='top'>You are calling an endpoint with invalid request data.</td>           <td valign='top'>Check the expected request format and try again.</td>       </tr>       </tbody>   </table> 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.1"

# import apis into sdk package
from nrf_cloud_client.api.account_api import AccountApi
from nrf_cloud_client.api.alerts_api import AlertsApi
from nrf_cloud_client.api.all_devices_api import AllDevicesApi
from nrf_cloud_client.api.anchors_api import AnchorsApi
from nrf_cloud_client.api.assisted_gps_api import AssistedGPSApi
from nrf_cloud_client.api.binary_logs_api import BinaryLogsApi
from nrf_cloud_client.api.bluetooth_low_energy_devices_api import BluetoothLowEnergyDevicesApi
from nrf_cloud_client.api.bulk_ops_requests_api import BulkOpsRequestsApi
from nrf_cloud_client.api.cell_location_api import CellLocationApi
from nrf_cloud_client.api.contribute_api import ContributeApi
from nrf_cloud_client.api.fota_job_executions_api import FOTAJobExecutionsApi
from nrf_cloud_client.api.fota_jobs_api import FOTAJobsApi
from nrf_cloud_client.api.firmware_bundles_api import FirmwareBundlesApi
from nrf_cloud_client.api.gnss_api import GNSSApi
from nrf_cloud_client.api.gateways_api import GatewaysApi
from nrf_cloud_client.api.geocoding_api import GeocodingApi
from nrf_cloud_client.api.ground_fix_api import GroundFixApi
from nrf_cloud_client.api.ip_devices_api import IPDevicesApi
from nrf_cloud_client.api.location_history_api import LocationHistoryApi
from nrf_cloud_client.api.messages_api import MessagesApi
from nrf_cloud_client.api.mqtt_team_devices_api import MqttTeamDevicesApi
from nrf_cloud_client.api.open_api_specification_api import OpenAPISpecificationApi
from nrf_cloud_client.api.predicted_gps_api import PredictedGPSApi
from nrf_cloud_client.api.single_cell_api import SingleCellApi
from nrf_cloud_client.api.system_status_api import SystemStatusApi
from nrf_cloud_client.api.wi_fi_location_api import WiFiLocationApi

# import ApiClient
from nrf_cloud_client.api_response import ApiResponse
from nrf_cloud_client.api_client import ApiClient
from nrf_cloud_client.configuration import Configuration
from nrf_cloud_client.exceptions import OpenApiException
from nrf_cloud_client.exceptions import ApiTypeError
from nrf_cloud_client.exceptions import ApiValueError
from nrf_cloud_client.exceptions import ApiKeyError
from nrf_cloud_client.exceptions import ApiAttributeError
from nrf_cloud_client.exceptions import ApiException

# import models into sdk package
from nrf_cloud_client.models.access_point import AccessPoint
from nrf_cloud_client.models.access_point_observation import AccessPointObservation
from nrf_cloud_client.models.access_point_with_channel import AccessPointWithChannel
from nrf_cloud_client.models.access_point_with_channel_observation import AccessPointWithChannelObservation
from nrf_cloud_client.models.access_point_with_frequency import AccessPointWithFrequency
from nrf_cloud_client.models.access_point_with_frequency_observation import AccessPointWithFrequencyObservation
from nrf_cloud_client.models.account_info_args import AccountInfoArgs
from nrf_cloud_client.models.account_info_args_plan import AccountInfoArgsPlan
from nrf_cloud_client.models.account_info_args_team import AccountInfoArgsTeam
from nrf_cloud_client.models.active_alert import ActiveAlert
from nrf_cloud_client.models.alert_status import AlertStatus
from nrf_cloud_client.models.alt_location_response import AltLocationResponse
from nrf_cloud_client.models.alternate_location import AlternateLocation
from nrf_cloud_client.models.anchor import Anchor
from nrf_cloud_client.models.anchor_input import AnchorInput
from nrf_cloud_client.models.anchor_meta import AnchorMeta
from nrf_cloud_client.models.anchor_update_input import AnchorUpdateInput
from nrf_cloud_client.models.api_limits_document_model import ApiLimitsDocumentModel
from nrf_cloud_client.models.api_usage_metrics_summary import ApiUsageMetricsSummary
from nrf_cloud_client.models.archived_alert import ArchivedAlert
from nrf_cloud_client.models.assistance_request import AssistanceRequest
from nrf_cloud_client.models.ble_device import BLEDevice
from nrf_cloud_client.models.ble_device_state_value import BLEDeviceStateValue
from nrf_cloud_client.models.ble_device_sub_type import BLEDeviceSubType
from nrf_cloud_client.models.ble_scan_config import BLEScanConfig
from nrf_cloud_client.models.ble_scan_config_filter import BLEScanConfigFilter
from nrf_cloud_client.models.ble_scan_type import BLEScanType
from nrf_cloud_client.models.bulk_ops_request_details import BulkOpsRequestDetails
from nrf_cloud_client.models.bulk_ops_request_endpoint import BulkOpsRequestEndpoint
from nrf_cloud_client.models.bulk_ops_request_status import BulkOpsRequestStatus
from nrf_cloud_client.models.c2_c_overages import C2COverages
from nrf_cloud_client.models.cell_observation import CellObservation
from nrf_cloud_client.models.cell_request import CellRequest
from nrf_cloud_client.models.cell_response_with_fulfillment import CellResponseWithFulfillment
from nrf_cloud_client.models.cell_service_type import CellServiceType
from nrf_cloud_client.models.characteristics_value import CharacteristicsValue
from nrf_cloud_client.models.characteristics_value_properties import CharacteristicsValueProperties
from nrf_cloud_client.models.commercial_services import CommercialServices
from nrf_cloud_client.models.contribute_location_data200_response import ContributeLocationData200Response
from nrf_cloud_client.models.contribution import Contribution
from nrf_cloud_client.models.contribution_item import ContributionItem
from nrf_cloud_client.models.create_fota_job201_response import CreateFOTAJob201Response
from nrf_cloud_client.models.create_job_input import CreateJobInput
from nrf_cloud_client.models.create_job_input_base import CreateJobInputBase
from nrf_cloud_client.models.create_job_input_criteria import CreateJobInputCriteria
from nrf_cloud_client.models.create_job_input_device_identifiers import CreateJobInputDeviceIdentifiers
from nrf_cloud_client.models.create_job_input_device_ids import CreateJobInputDeviceIds
from nrf_cloud_client.models.create_job_input_id_or_identifier import CreateJobInputIdOrIdentifier
from nrf_cloud_client.models.create_job_input_tags import CreateJobInputTags
from nrf_cloud_client.models.create_job_input_tags_and_device_ids import CreateJobInputTagsAndDeviceIds
from nrf_cloud_client.models.create_job_input_tags_bundle_id import CreateJobInputTagsBundleId
from nrf_cloud_client.models.create_soft_gateway_payload import CreateSoftGatewayPayload
from nrf_cloud_client.models.d2_c_overages import D2COverages
from nrf_cloud_client.models.deprecated_ground_fix_request import DeprecatedGroundFixRequest
from nrf_cloud_client.models.descriptors_value import DescriptorsValue
from nrf_cloud_client.models.developer_plan import DeveloperPlan
from nrf_cloud_client.models.device import Device
from nrf_cloud_client.models.device_alert import DeviceAlert
from nrf_cloud_client.models.device_certificate import DeviceCertificate
from nrf_cloud_client.models.device_count_by_type import DeviceCountByType
from nrf_cloud_client.models.device_doc_meta import DeviceDocMeta
from nrf_cloud_client.models.device_doc_meta_args import DeviceDocMetaArgs
from nrf_cloud_client.models.device_doc_meta_args_created_at import DeviceDocMetaArgsCreatedAt
from nrf_cloud_client.models.device_firmware_args import DeviceFirmwareArgs
from nrf_cloud_client.models.device_firmware_args_app import DeviceFirmwareArgsApp
from nrf_cloud_client.models.device_message import DeviceMessage
from nrf_cloud_client.models.device_message_input import DeviceMessageInput
from nrf_cloud_client.models.device_message_input_message import DeviceMessageInputMessage
from nrf_cloud_client.models.device_shadow import DeviceShadow
from nrf_cloud_client.models.device_state_input import DeviceStateInput
from nrf_cloud_client.models.device_types import DeviceTypes
from nrf_cloud_client.models.device_types_ble import DeviceTypesBLE
from nrf_cloud_client.models.device_types_gateway import DeviceTypesGateway
from nrf_cloud_client.models.device_types_generic import DeviceTypesGeneric
from nrf_cloud_client.models.do_reply_flag import DoReplyFlag
from nrf_cloud_client.models.enterprise_per_device_billing_model_plan import EnterprisePerDeviceBillingModelPlan
from nrf_cloud_client.models.extract_plan_types_developer import ExtractPlanTypesDEVELOPER
from nrf_cloud_client.models.extract_plan_types_enterprise import ExtractPlanTypesENTERPRISE
from nrf_cloud_client.models.fota_job_execution import FOTAJobExecution
from nrf_cloud_client.models.fota_job_execution_state import FOTAJobExecutionState
from nrf_cloud_client.models.fotav2_job import FOTAV2Job
from nrf_cloud_client.models.fotav2_job_execution_stats import FOTAV2JobExecutionStats
from nrf_cloud_client.models.fotav2_job_firmware import FOTAV2JobFirmware
from nrf_cloud_client.models.fotav2_job_firmware_bundle_id import FOTAV2JobFirmwareBundleId
from nrf_cloud_client.models.fetch_device200_response import FetchDevice200Response
from nrf_cloud_client.models.fetch_fota_job_execution200_response import FetchFOTAJobExecution200Response
from nrf_cloud_client.models.fetch_fota_job_execution200_response_any_of import FetchFOTAJobExecution200ResponseAnyOf
from nrf_cloud_client.models.fetch_fota_job_execution200_response_any_of_job_document import FetchFOTAJobExecution200ResponseAnyOfJobDocument
from nrf_cloud_client.models.file_download_info import FileDownloadInfo
from nrf_cloud_client.models.firmware import Firmware
from nrf_cloud_client.models.firmware_types import FirmwareTypes
from nrf_cloud_client.models.fota_job_v2_plus import FotaJobV2Plus
from nrf_cloud_client.models.fota_job_v2_plus_target import FotaJobV2PlusTarget
from nrf_cloud_client.models.fota_v2_job_document_model import FotaV2JobDocumentModel
from nrf_cloud_client.models.fota_v2_job_events import FotaV2JobEvents
from nrf_cloud_client.models.fota_v2_job_execution_events import FotaV2JobExecutionEvents
from nrf_cloud_client.models.fota_v2_job_target_model import FotaV2JobTargetModel
from nrf_cloud_client.models.gps_location_services import GPSLocationServices
from nrf_cloud_client.models.gateway_device import GatewayDevice
from nrf_cloud_client.models.gateway_device_sub_type import GatewayDeviceSubType
from nrf_cloud_client.models.generate_service_key_and_token200_response import GenerateServiceKeyAndToken200Response
from nrf_cloud_client.models.generic_device import GenericDevice
from nrf_cloud_client.models.generic_device_state import GenericDeviceState
from nrf_cloud_client.models.generic_device_sub_type import GenericDeviceSubType
from nrf_cloud_client.models.geocode_location_services import GeocodeLocationServices
from nrf_cloud_client.models.get_location_from_cells_or_wifi_networks_request import GetLocationFromCellsOrWifiNetworksRequest
from nrf_cloud_client.models.get_predicted_assistance_data200_response import GetPredictedAssistanceData200Response
from nrf_cloud_client.models.get_service_token200_response import GetServiceToken200Response
from nrf_cloud_client.models.get_single_cell_location200_response import GetSingleCellLocation200Response
from nrf_cloud_client.models.gnss_meta import GnssMeta
from nrf_cloud_client.models.gps_request import GpsRequest
from nrf_cloud_client.models.ground_fix_location_service import GroundFixLocationService
from nrf_cloud_client.models.ground_fix_location_services import GroundFixLocationServices
from nrf_cloud_client.models.ground_fix_request import GroundFixRequest
from nrf_cloud_client.models.ground_fix_response_with_fulfillment import GroundFixResponseWithFulfillment
from nrf_cloud_client.models.ground_fix_response_with_fulfillment_fulfilled_with import GroundFixResponseWithFulfillmentFulfilledWith
from nrf_cloud_client.models.ground_fix_service_type import GroundFixServiceType
from nrf_cloud_client.models.hard_gateway_sub_type import HardGatewaySubType
from nrf_cloud_client.models.identity_service_type import IdentityServiceType
from nrf_cloud_client.models.invoice_response import InvoiceResponse
from nrf_cloud_client.models.invoice_status_events import InvoiceStatusEvents
from nrf_cloud_client.models.job_schedule import JobSchedule
from nrf_cloud_client.models.location_contribution import LocationContribution
from nrf_cloud_client.models.location_service_type import LocationServiceType
from nrf_cloud_client.models.location_service_type_mcell import LocationServiceTypeMCELL
from nrf_cloud_client.models.location_service_type_mcelleval import LocationServiceTypeMCELLEVAL
from nrf_cloud_client.models.location_service_type_scell import LocationServiceTypeSCELL
from nrf_cloud_client.models.location_service_type_scelleval import LocationServiceTypeSCELLEVAL
from nrf_cloud_client.models.location_service_type_wifi import LocationServiceTypeWIFI
from nrf_cloud_client.models.location_service_type_wifieval import LocationServiceTypeWIFIEVAL
from nrf_cloud_client.models.location_service_usage import LocationServiceUsage
from nrf_cloud_client.models.location_services import LocationServices
from nrf_cloud_client.models.location_tracker_item import LocationTrackerItem
from nrf_cloud_client.models.lte_cell import LteCell
from nrf_cloud_client.models.lte_contribution import LteContribution
from nrf_cloud_client.models.lte_neighbor_measurement import LteNeighborMeasurement
from nrf_cloud_client.models.message import Message
from nrf_cloud_client.models.messages_service_type import MessagesServiceType
from nrf_cloud_client.models.metric_source import MetricSource
from nrf_cloud_client.models.mnc import Mnc
from nrf_cloud_client.models.non_gateway_ip_device_sub_type import NonGatewayIPDeviceSubType
from nrf_cloud_client.models.non_location_services import NonLocationServices
from nrf_cloud_client.models.nrf_gps_message_type import NrfGpsMessageType
from nrf_cloud_client.models.nrf_message_type import NrfMessageType
from nrf_cloud_client.models.observing_device import ObservingDevice
from nrf_cloud_client.models.onboard_devices202_response import OnboardDevices202Response
from nrf_cloud_client.models.onboard_single_device_args import OnboardSingleDeviceArgs
from nrf_cloud_client.models.overage_c2_c_base import OverageC2CBase
from nrf_cloud_client.models.overage_d2_c_base import OverageD2CBase
from nrf_cloud_client.models.overages import Overages
from nrf_cloud_client.models.page_sort import PageSort
from nrf_cloud_client.models.paginated_result_anchor import PaginatedResultAnchor
from nrf_cloud_client.models.paginated_result_bulk_ops_request_details import PaginatedResultBulkOpsRequestDetails
from nrf_cloud_client.models.paginated_result_contribution_item import PaginatedResultContributionItem
from nrf_cloud_client.models.paginated_result_device_alert import PaginatedResultDeviceAlert
from nrf_cloud_client.models.paginated_result_device_message import PaginatedResultDeviceMessage
from nrf_cloud_client.models.paginated_result_device_or_jso_nata_transformed_response import PaginatedResultDeviceOrJSONataTransformedResponse
from nrf_cloud_client.models.paginated_result_device_or_jso_nata_transformed_response_items_inner import PaginatedResultDeviceOrJSONataTransformedResponseItemsInner
from nrf_cloud_client.models.paginated_result_device_tag import PaginatedResultDeviceTag
from nrf_cloud_client.models.paginated_result_device_tag_or_jso_nata_transformed_response import PaginatedResultDeviceTagOrJSONataTransformedResponse
from nrf_cloud_client.models.paginated_result_device_tag_or_jso_nata_transformed_response_items_inner import PaginatedResultDeviceTagOrJSONataTransformedResponseItemsInner
from nrf_cloud_client.models.paginated_result_fota_job_execution import PaginatedResultFOTAJobExecution
from nrf_cloud_client.models.paginated_result_fota_job_execution_state import PaginatedResultFOTAJobExecutionState
from nrf_cloud_client.models.paginated_result_fotav2_job_or_fota_job_v2_plus import PaginatedResultFOTAV2JobOrFotaJobV2Plus
from nrf_cloud_client.models.paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner import PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner
from nrf_cloud_client.models.paginated_result_firmware import PaginatedResultFirmware
from nrf_cloud_client.models.paginated_result_invoice_response import PaginatedResultInvoiceResponse
from nrf_cloud_client.models.paginated_result_location_tracker_item import PaginatedResultLocationTrackerItem
from nrf_cloud_client.models.paginated_result_omit_api_usage_metric_record_tenant_id import PaginatedResultOmitApiUsageMetricRecordTenantId
from nrf_cloud_client.models.pick_api_usage_metric_record_exclude_keyof_api_usage_metric_record_tenant_id import PickApiUsageMetricRecordExcludeKeyofApiUsageMetricRecordTenantId
from nrf_cloud_client.models.pick_bulk_ops_request_exclude_keyof_bulk_ops_request_tenant_id_or_metadata import PickBulkOpsRequestExcludeKeyofBulkOpsRequestTenantIdOrMetadata
from nrf_cloud_client.models.pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id import PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId
from nrf_cloud_client.models.pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type import PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageType
from nrf_cloud_client.models.pick_invoice_line_item_non_overage_exclude_keyof_invoice_line_item_non_overage_type_service_id import PickInvoiceLineItemNonOverageExcludeKeyofInvoiceLineItemNonOverageTypeServiceId
from nrf_cloud_client.models.pick_plan_types_exclude_keyof_plan_types_developer import PickPlanTypesExcludeKeyofPlanTypesDEVELOPER
from nrf_cloud_client.models.pick_record_location_services_location_service_usage_exclude_keyof_record_location_services_location_service_usage_groundfix import PickRecordLocationServicesLocationServiceUsageExcludeKeyofRecordLocationServicesLocationServiceUsageGROUNDFIX
from nrf_cloud_client.models.position_response import PositionResponse
from nrf_cloud_client.models.position_response_with_extras import PositionResponseWithExtras
from nrf_cloud_client.models.pro_or_higher_plan import ProOrHigherPlan
from nrf_cloud_client.models.provisioning_service_type import ProvisioningServiceType
from nrf_cloud_client.models.proxy_usage_declarations import ProxyUsageDeclarations
from nrf_cloud_client.models.record_gnss_coordinates_request import RecordGnssCoordinatesRequest
from nrf_cloud_client.models.request_type import RequestType
from nrf_cloud_client.models.rest_api_payload_content_type_with_csv import RestApiPayloadContentTypeWithCsv
from nrf_cloud_client.models.rest_api_payload_content_type_with_zip import RestApiPayloadContentTypeWithZip
from nrf_cloud_client.models.reverse_geo_address import ReverseGeoAddress
from nrf_cloud_client.models.reverse_geo_response import ReverseGeoResponse
from nrf_cloud_client.models.service import Service
from nrf_cloud_client.models.service_key_info import ServiceKeyInfo
from nrf_cloud_client.models.service_key_token_response import ServiceKeyTokenResponse
from nrf_cloud_client.models.service_key_type import ServiceKeyType
from nrf_cloud_client.models.service_type_value import ServiceTypeValue
from nrf_cloud_client.models.service_usage_summary import ServiceUsageSummary
from nrf_cloud_client.models.single_cell_format import SingleCellFormat
from nrf_cloud_client.models.soft_gateway_type import SoftGatewayType
from nrf_cloud_client.models.tagged_bundle_id import TaggedBundleId
from nrf_cloud_client.models.target_list_type import TargetListType
from nrf_cloud_client.models.tenant_user_role import TenantUserRole
from nrf_cloud_client.models.tracker_service_type import TrackerServiceType
from nrf_cloud_client.models.update_fota_job_execution_status_request import UpdateFOTAJobExecutionStatusRequest
from nrf_cloud_client.models.update_job_input import UpdateJobInput
from nrf_cloud_client.models.upload_firmware202_response import UploadFirmware202Response
from nrf_cloud_client.models.usage_metric_date import UsageMetricDate
from nrf_cloud_client.models.wifi_access_points_request import WifiAccessPointsRequest
