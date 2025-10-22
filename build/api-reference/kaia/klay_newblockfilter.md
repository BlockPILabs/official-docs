---
description: Creates a filter in the node, to notify when a new block arrives.
---

# kaia\_newBlockFilter

The execution of this API can be limited by two node configurations to manage resources of Klaytn node safely.

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
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_newBlockFilter","params":[],"id":73}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":73,
  "result":"0xc2f2e8168a7e38b5d979d0f7084130ee"
}
```
{% endcode %}
