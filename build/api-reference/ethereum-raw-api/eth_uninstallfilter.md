---
description: >-
  Uninstalls a filter with a given id. Should always be called when a watch is
  no longer needed. Additionally, filters timeout when they aren’t requested
  with eth_getFilterChanges for some time.
---

# eth\_uninstallFilter

#### **Parameters:**

**QUANTITY** - the filter id.

#### **Returns:**

**Boolean** - true if the filter was successfully uninstalled, otherwise false.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://arc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_uninstallFilter","params":["0x8d541bd87a8dd2beb1aa2cdcf353a986"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": true
}
```
{% endcode %}
