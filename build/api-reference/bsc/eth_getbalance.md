---
description: Returns the balance of the account of the given address.
---

# eth\_getBalance

#### **Parameters:**

**DATA, 20 Bytes** - address to check for balance.

**QUANTITY|TAG** - integer block number, or the string "latest"

#### **Returns:**

**QUANTITY** - integer of the current balance in wei.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0xF598452bfC73b34bF74cef41327Cf0D9f76b4B62", "latest"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x1773ec0fb477760"
}
```
{% endcode %}
