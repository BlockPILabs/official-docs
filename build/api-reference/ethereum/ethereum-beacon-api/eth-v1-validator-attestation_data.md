# /eth/v1/validator/attestation\_data

Requests that the beacon node produce an AttestationData.

A 503 error must be returned if the block identified by the response `beacon_block_root` is optimistic (i.e. the attestation attests to a block that has not been fully verified by an execution engine).

#### Parameters:

**slot-string**, The slot for which the block should be proposed.

**committee\_index-strin**g, The validator's randao reveal value.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/attestation_data?slot=9091263&committee_index=1

// Result

```
{% endcode %}
