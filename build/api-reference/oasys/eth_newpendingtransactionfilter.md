---
description: >-
  Creates a filter in the node, to notify when new pending transactions arrive.
  To check if the state has changed, call eth_getFilterChanges.
---

# eth\_newPendingTransactionFilter

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - A filter id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://oasys.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xf38058ac2ca4e5dcabd335362bcacfab"
}
```
{% endcode %}
