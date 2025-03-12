---
description: Get the most recent accepted block number
---

# starknet\_blockNumber

#### **Parameters:**

**None**

#### **Returns:**

The latest block number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_blockNumber","params":[],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": 472483
}
```
{% endcode %}
