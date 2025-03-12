---
description: Returns the version of the Starknet JSON-RPC specification being used
---

# starknet\_specVersion

#### **Parameters:**

None

#### **Returns:**

**String** - The current Starknet JSON-RPC specification

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_specVersion","params":[],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0.5.1"
}
```
{% endcode %}
