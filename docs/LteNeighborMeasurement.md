# LteNeighborMeasurement

Neighbor cell information. Can increase location accuracy when included in request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsrp** | **float** | Reference Signal Received Power. Measured in dBm. See &lt;a href&#x3D;\&quot;https://www.rfwireless-world.com/Terminology/LTE-RSRP-vs-RSRQ.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this page&lt;/a&gt; for more details. Range -157..-44 | [optional] 
**rsrq** | **float** | Reference Signal Received Quality. Measured in dB. See &lt;a href&#x3D;\&quot;https://www.rfwireless-world.com/Terminology/LTE-RSRP-vs-RSRQ.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this page&lt;/a&gt; for more details. Range -34.5..3.5 | [optional] 
**earfcn** | **int** | Evolved Absolute Radio Frequency Channel (E-ARFCN). Range: 0..262143. See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/136100_136199/136106/17.00.00_60/ts_136106v170000p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 136 106, section 5.7.3&lt;/a&gt; for more details. | 
**pci** | **int** | Physical Cell Identity (PCI). Used in the physical layer of E-UTRA systems to identify a cell. Range: 0..503 | 
**eci** | **int** | E-UTRA Cell Identifier (ECI), 28 bits (20 bits eNodeB and 8 bits Cell ID). Calculated using \&quot;(eNodeB-ID * 256) + Sector-ID\&quot;. Range 0 .. 268435455. See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/123000_123099/123003/17.09.00_60/ts_123003v170900p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 123 003, section 19.6&lt;/a&gt; for more details. | [optional] 
**time_diff** | **float** | Milliseconds that the neighbor cell was observed after the serving cell was observed. Improves accuracy for devices in motion. | [optional] 

## Example

```python
from nrf_cloud_client.models.lte_neighbor_measurement import LteNeighborMeasurement

# TODO update the JSON string below
json = "{}"
# create an instance of LteNeighborMeasurement from a JSON string
lte_neighbor_measurement_instance = LteNeighborMeasurement.from_json(json)
# print the JSON string representation of the object
print(LteNeighborMeasurement.to_json())

# convert the object into a dict
lte_neighbor_measurement_dict = lte_neighbor_measurement_instance.to_dict()
# create an instance of LteNeighborMeasurement from a dict
lte_neighbor_measurement_from_dict = LteNeighborMeasurement.from_dict(lte_neighbor_measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


