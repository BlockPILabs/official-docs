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
curl https://linea.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0xeb96f72d00ed0831805d41c2b7bfa7305a3c088c238ceb1dbcc0aeb3fed921a9"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xa"
}
```
{% endcode %}
