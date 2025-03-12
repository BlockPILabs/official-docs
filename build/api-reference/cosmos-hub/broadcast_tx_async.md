---
description: >-
  Returns right away, with no response. Does not wait for CheckTx nor DeliverTx
  Response.
---

# /broadcast\_tx\_async

#### **Parameters:**

**tx - string**, The transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/broadcast_tx_async?tx=<the transaction>

// Result
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "code": "0",
    "data": "",
    "log": "",
    "codespace": "ibc",
    "hash": "0D33F2F03A5234F38706E43004489E061AC40A2E"
  },
  "error": ""
}                         
```
{% endcode %}
