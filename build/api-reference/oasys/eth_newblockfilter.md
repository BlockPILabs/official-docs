---
description: >-
  Creates a filter in the node, to notify when a new block arrives. To check if
  the state has changed, call eth_getFilterChanges.
---

# eth\_newBlockFilter

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - A filter id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://oasys.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newBlockFilter","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x37f5a49b57a1a9bda74c8c1cdfe7fc71"
}
```
{% endcode %}
