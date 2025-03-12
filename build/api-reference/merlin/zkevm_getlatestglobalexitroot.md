---
description: Returns the latest block number that is connected to the latest batch verified
---

# zkevm\_getLatestGlobalExitRoot

**Parameters:**

**None**

**Returns:**

**String** - Hex representation of a Keccak 256 hash

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
{
    "jsonrpc": "2.0",
    "method": "zkevm_getLatestGlobalExitRoot",
    "params": [],
    "id": 1
}

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5"
}
```
{% endcode %}
