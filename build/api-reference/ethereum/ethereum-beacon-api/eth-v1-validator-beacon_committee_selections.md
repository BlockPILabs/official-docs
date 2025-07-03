# /eth/v1/validator/beacon\_committee\_selections

This endpoint should be used by a validator client running as part of a distributed validator cluster, and is implemented by a distributed validator middleware client. This endpoint is used to exchange partial selection proofs for combined/aggregated selection proofs to allow a validator client to correctly determine if any of its validators has been selected to perform an attestation aggregation duty in a slot. Validator clients running in a distributed validator cluster must query this endpoint at the start of an epoch for the current and lookahead (next) epochs for all validators that have attester duties in the current and lookahead epochs. Consensus clients need not support this endpoint and may return a 501.

#### Parameters:

**None**

**Request body:**

array\<object>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/beacon_committee_selections
'
[
  {
    "validator_index": "1",
    "slot": "1",
    "selection_proof": "0x1b66ac1fb663c9bc59509846d6ec05345bd908eda73e670af888da41af171505cc411d61252fb6cb3fa0017b679f8bb2305b26a285fa2737f175668d0dff91cc1b66ac1fb663c9bc59509846d6ec05345bd908eda73e670af888da41af171505"
  }
]
'

// Result

```
{% endcode %}
