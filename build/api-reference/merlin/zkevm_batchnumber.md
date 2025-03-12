---
description: Returns the latest batch number
---

# zkevm\_batchNumber

**Parameters:**

**None**

**Returns:**

**String** - the hex representation of latest batch number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json"
--data '{"jsonrpc":"2.0","method":"zkevm_batchNumber","params":[],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x1dbb1c"
}
```
{% endcode %}
