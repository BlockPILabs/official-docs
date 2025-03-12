---
description: Retrieves number of known peers.
---

# /eth/v1/node/peer\_count



#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/node/peer_count

// Result
{
    "data": {
        "connected": "103",
        "connecting": "0",
        "disconnected": "655",
        "disconnecting": "2"
    }
}
```
{% endcode %}
