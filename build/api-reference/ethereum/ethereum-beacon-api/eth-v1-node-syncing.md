---
description: >-
  Requests the beacon node to describe if it's currently syncing or not, and if
  it is, what block it is up to.
---

# /eth/v1/node/syncing



#### Parameters:

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/node/syncing

// Result
{
    "data": {
        "is_syncing": false,
        "is_optimistic": false,
        "el_offline": false,
        "head_slot": "9091172",
        "sync_distance": "0"
    }
}
```
{% endcode %}
