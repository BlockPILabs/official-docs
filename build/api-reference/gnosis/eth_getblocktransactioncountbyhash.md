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
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0xf763dcf18ee553e1ca8bd5360d065e9ce3453383502a6a2c9dadf1646bb6a2e7"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": "0x1",
    "id": 1
}
```
{% endcode %}
