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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x407d73d8a49eeb85d32cf465507dd71d507100c1", "latest"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x0"
}
```
{% endcode %}
