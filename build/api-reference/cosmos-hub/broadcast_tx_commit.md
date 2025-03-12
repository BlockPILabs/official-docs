---
description: Returns with the responses from CheckTx and DeliverTx.
---

# /broadcast\_tx\_commit

#### **Parameters:**

**tx - string**, The transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/broadcast_tx_commit?tx=<the transaction>

// Result
{
  "error": "",
  "result": {
    "height": "26682",
    "hash": "75CA0F856A4DA078FC4911580360E70CEFB2EBEE",
    "deliver_tx": {
      "log": "",
      "data": "",
      "code": "0"
    },
    "check_tx": {
      "log": "",
      "data": "",
      "code": "0"
    }
  },
  "id": 0,
  "jsonrpc": "2.0"
}                        
```
{% endcode %}
