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
curl https://meter.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getCode","params":["0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b", "0x2"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x"
}
```
{% endcode %}
