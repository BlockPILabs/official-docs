---
description: Returns the number of transactions in a block matching the given block number.
---

# eth\_getBlockTransactionCountByHash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

#### **Returns:**

**QUANTITY** - integer of the number of transactions in this block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x744a3dac0d390c212fbc318972bc9200d8c9aff01ae4f063634343457d30fbc9"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x1"
}
```
{% endcode %}
