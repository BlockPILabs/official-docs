---
description: Returns number of peers currently connected to the client.
---

# net\_peerCount

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the number of connected peers.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xc8"
}
```
{% endcode %}
