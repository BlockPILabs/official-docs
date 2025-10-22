---
description: Creates a filter in the node, to notify when new pending transactions arrive.
---

# kaia\_newPendingTransactionFilter

#### **Parameters**

None

#### **Return Value**

| Type     | Description  |
| -------- | ------------ |
| QUANTITY | A filter id. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_newPendingTransactionFilter","params":[],"id":73}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":73,
  "result":"0x90cec22a723fcc725fb2462733c2880f"
}
```
{% endcode %}
