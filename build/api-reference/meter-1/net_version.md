---
description: Returns the current network id.
---

# net\_version

#### **Parameters:**

None

#### **Returns:**

**String** - The current network id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://monad.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"net_version","params":[],"id":83}'

// Result
{
    "jsonrpc": "2.0",
    "result": "10143",
    "id": 774997591
}
```
{% endcode %}
