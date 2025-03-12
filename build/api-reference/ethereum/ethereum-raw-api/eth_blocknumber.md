---
description: Returns the number of the most recent block.
---

# eth\_blockNumber

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the current block number the client is on.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xf2f8c7"
}
```
{% endcode %}
