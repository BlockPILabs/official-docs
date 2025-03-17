---
description: Returns an RLP-encoded block.
---

# debug\_getRawBlock

#### **Parameters:**

**QUANTITY|TAG** - Integer block number encoded as a hexadecimal, or the string 'latest', 'earliest' or 'pending'.

**QUANTITY** - A hex of the integer representing the position in the block.

#### **Returns:**

**String**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://monad.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_getRawBlock","params":["0x7c2de7"],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": -
}
```
{% endcode %}
