# /eth/v1/validator/aggregate\_attestation

Aggregates all attestations matching given attestation data root and slot.

A 503 error must be returned if the block identified by the response `beacon_block_root` is optimistic (i.e. the aggregated attestation attests to a block that has not been fully verified by an execution engine).

A 404 error must be returned if no attestation is available for the requested `attestation_data_root`.

#### Parameters:

**attestation\_data\_root-string**, HashTreeRoot of AttestationData that validator wants aggregated

**slot-strin**g, The slot for which the block should be proposed.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/aggregate_attestation?attestation_data_root=0xcf8e0d4e9587369b2301d0790347320302cc0943d5a1884560367e8208d920f2&slot=9091319%20

// Result

```
{% endcode %}
