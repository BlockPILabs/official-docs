---
description: >-
  Calculates HashTreeRoot for state with given 'stateId'. If stateId is root,
  same value will be returned.
---

# /eth/v1/beacon/states/{state\_id}/root

#### **Parameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/finalized/root

// Result
{
    "execution_optimistic": false,
    "finalized": true,
    "data": {
        "root": "0x30d025d9ad1d3dccdb71a011051c5f864bfedee7c6ba03a37d9cdb7e4c3f77b5"
    }
}
```
{% endcode %}
