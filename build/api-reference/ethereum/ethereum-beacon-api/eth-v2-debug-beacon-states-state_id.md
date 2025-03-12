---
description: >-
  Returns full BeaconState object for given stateId. Depending on Accept header
  it can be returned either as json or as bytes serialized by SSZ
---

# /eth/v2/debug/beacon/states/{state\_id}



#### Parameters:

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v2/debug/beacon/states/head

// Result

```
{% endcode %}
