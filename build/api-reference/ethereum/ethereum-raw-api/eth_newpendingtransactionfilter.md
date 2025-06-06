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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x8d394290681fcb2ec58fcc21224163c067aa1b6ba20c98a42786b364065380b3"
}
```
{% endcode %}
