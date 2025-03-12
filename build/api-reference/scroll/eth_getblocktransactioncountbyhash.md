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
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x3d3443a85596bfa9baa32ec9ee826ccc726a34574cffe43474f1fe6a368b5b3a"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x1"
}
```
{% endcode %}
