---
description: Get the most recent accepted block hash and number
---

# starknet\_blockHashAndNumber

#### **Parameters:**

**None**

#### **Returns:**

The latest block hash and number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_blockHashAndNumber","params":[],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "block_hash": "0x71e608d343ff70f3baa49504ca9b9ec33cd16449222c3bf6922518c296e1e78",
        "block_number": 472485
    }
}
```
{% endcode %}
