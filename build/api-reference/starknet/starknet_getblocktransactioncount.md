---
description: >-
  Returns the receipt of a transaction by transaction hash. Note That the
  receipt is not available for pending transactions.
---

# starknet\_getBlockTransactionCount

#### **Parameters:**

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`

#### **Returns:**

The number of transactions in the designated block

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getBlockTransactionCount","params": ["latest"],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": 127
}
```
{% endcode %}
