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
```python
// Request
curl https://arc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0xb84173b6534d0cee34905b621f21e5e518c464feb549f1372640b3fec137b3b2"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xcc"
}
```
{% endcode %}
