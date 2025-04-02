---
description: Returns the number of transactions in a block matching the given block number.
---

# eth\_getBlockTransactionCountByHash

#### **Parameters:**

**DATA , 32 Bytes** - Hash of a block.

#### **Returns:**

**QUANTITY** - integer of the number of transactions in this block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x8a7c32a1810f6b940bb46aa0c569d3c0f01a6e5fbb2d9f471cb2124b5eccea29"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x1"
}
```
{% endcode %}
