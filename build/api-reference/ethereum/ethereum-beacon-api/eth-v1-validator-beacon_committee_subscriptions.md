# /eth/v1/validator/beacon\_committee\_subscriptions

After beacon node receives this request, search using discv5 for peers related to this subnet and replace current peers with those ones if necessary If validator `is_aggregator`, beacon node must:

* announce subnet topic subscription on gossipsub
* aggregate attestations received on that subnet

#### Parameters:

**None**

**Request body:**

array\<object>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/aggregate_and_proofs
'
[
  {
    "validator_index": "1",
    "committee_index": "1",
    "committees_at_slot": "1",
    "slot": "1",
    "is_aggregator": true
  }
]
'

// Result

```
{% endcode %}
