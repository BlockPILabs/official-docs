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
curl https://avalanche.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newBlockFilter","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xdbbebdc0d4dccb42eec0ea4cc231af0b"
}
```
{% endcode %}
