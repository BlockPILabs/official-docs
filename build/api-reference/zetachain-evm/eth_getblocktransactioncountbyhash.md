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
curl https://zetachain-evm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x6abdf078b2d4a9d0890c6e9ef3136d10d944b92240762c62e6971a09054814fe"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x0"
}
```
{% endcode %}
