---
description: returns the base fee for the next big block
---

# eth\_bigBlockGasPrice

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the current gas price in wei.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_bigBlockGasPrice","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": "0x5f5e100",
    "id": 1
}
```
{% endcode %}
