---
description: Returns Fork object for state with given 'stateId'.
---

# /eth/v1/beacon/states/{state\_id}/fork

#### **Parameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/finalized/fork

// Result
{
    "execution_optimistic": false,
    "finalized": true,
    "data": {
        "previous_version": "0x03000000",
        "current_version": "0x04000000",
        "epoch": "269568"
    }
}
```
{% endcode %}
