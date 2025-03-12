---
description: Returns code at a given address.
---

# eth\_getCode

#### **Parameters:**

**DATA, 20 Bytes** - address

**QUANTITY|TAG** - integer block number, or the string "latest"

#### **Returns:**

**DATA** - the code from the given address.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://artela-testnet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getCode","params":[artela-testnet],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x"
}
```
{% endcode %}
