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
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xa0d677de0b2c488d6252be76a10e74db"
}
```
{% endcode %}
