---
description: Retrieves all possible chain heads (leaves of fork choice tree).
---

# /eth/v2/debug/beacon/heads



#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v2/debug/beacon/heads

// Result
{
    "data": [
        {
            "slot": "9091072",
            "root": "0x08d3f1a6b837006bb10046bab46c12abace10cf406dfe1d8d9ab600da3fa0cb1",
            "execution_optimistic": false
        }
    ]
}
```
{% endcode %}
