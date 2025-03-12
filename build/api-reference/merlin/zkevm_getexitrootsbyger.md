---
description: Gets the exit roots accordingly to the provided Global Exit Root
---

# zkevm\_getExitRootsByGER

**Parameters:**

**String** - Hex representation of a Keccak 256 hash

**Returns:**

**Object** - Exit roots result, or null when no block was found

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
{
    "jsonrpc": "2.0",
    "method": "zkevm_getExitRootsByGER",
    "params": ["0xad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5"],
    "id": 1
}

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockNumber": "0x153ab",
        "timestamp": "0xfffffff1886e0900",
        "mainnetExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "rollupExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000000"
    }
}
```
{% endcode %}
