---
description: >-
  Returns finality checkpoints for state with given 'stateId'. In case finality
  is not yet achieved, checkpoint should return epoch 0 and ZERO_HASH as root.
---

# /eth/v1/beacon/states/{state\_id}/finality\_checkpoints

#### **Parameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/finalized/finality_checkpoints

// Result
{
    "execution_optimistic": false,
    "finalized": true,
    "data": {
        "previous_justified": {
            "epoch": "283874",
            "root": "0x403046c912ec6e8cb244ee4d0bfc067e083c3dc980b584b8808052e4566a22cb"
        },
        "current_justified": {
            "epoch": "283875",
            "root": "0x0d69d9c458221fb0efb5a87a37138c058fbc77a7441f5f248f5774386603e4d4"
        },
        "finalized": {
            "epoch": "283874",
            "root": "0x403046c912ec6e8cb244ee4d0bfc067e083c3dc980b584b8808052e4566a22cb"
        }
    }
}
```
{% endcode %}
