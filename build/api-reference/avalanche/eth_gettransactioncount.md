---
description: Returns the number of transactions sent from an address.
---

# eth\_getTransactionCount

#### **Parameters:**

**DATA, 20 Bytes** - address.

**QUANTITY|TAG** - integer block number, or the string "latest"

#### **Returns:**

**QUANTITY** - integer of the number of transactions send from this address.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://avalanche.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params":["0x2737840364fba5642f96ea530f21a43e69a70f59","latest"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x11c"
}
```
{% endcode %}
