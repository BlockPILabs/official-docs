---
description: >-
  Returns a list of addresses owned by client. Since BlockPI does not store
  keys, this will always return empty.
---

# eth\_accounts

#### **Parameters:**

None

#### **Returns:**

**Array: DATA, 20 Bytes -** addresses owned by the client.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"eth_accounts","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": []
}
```
{% endcode %}
