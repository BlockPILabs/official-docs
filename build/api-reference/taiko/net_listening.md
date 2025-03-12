---
description: Returns true if a client is actively listening for network connections.
---

# net\_listening

#### **Parameters:**

None

#### **Returns:**

**Boolean** - true when listening, otherwise false.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://taiko-hekla.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"net_listening","params":[],"id":83}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": true
}
```
{% endcode %}
