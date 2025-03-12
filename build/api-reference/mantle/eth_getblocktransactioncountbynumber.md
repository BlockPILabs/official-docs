---
description: Returns the number of transactions in a block matching the given block number.
---

# eth\_getBlockTransactionCountByNumber

#### **Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "latest"

#### **Returns:**

**QUANTITY** - integer of the number of transactions in this block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://mantle.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params":["latest"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x14"
}
```
{% endcode %}
