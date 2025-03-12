# /eth/v1/validator/sync\_committee\_subscriptions

Subscribe to a number of sync committee subnets

Sync committees are not present in phase0, but are required for Altair networks.

Subscribing to sync committee subnets is an action performed by VC to enable network participation in Altair networks, and only required if the VC has an active validator in an active sync committee.

#### Parameters:

**None**

**Request body:**

array\<object>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/sync_committee_subscriptions
'
[
  {
    "validator_index": "1",
    "sync_committee_indices": [
      "1"
    ],
    "until_epoch": "1"
  }
]
'

// Result

```
{% endcode %}
