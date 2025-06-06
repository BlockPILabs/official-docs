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
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params":["0x17281460228691b044e080a5f5257dce8e47f79c","latest"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x30"
}
```
{% endcode %}
