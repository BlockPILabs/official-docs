---
description: returns whether the address is using big blocks
---

# eth\_usingBigBlocks

#### **Parameters:**

**DATA, 20 Bytes** - address

#### **Returns:**

**Boolean (FALSE)** - the address is not using big blocks

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_bigBlockGasPrice","params":["0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": false,
    "id": 1
}
```
{% endcode %}
