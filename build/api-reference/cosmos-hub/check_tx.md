---
description: Checks the transaction without executing it.
---

# /check\_tx

#### **Parameters:**

**tx - string**, The transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/check_tx?tx=<the transaction>

// Result
{
  "error": "",
  "result": {
    "code": "0",
    "data": "",
    "log": "",
    "info": "",
    "gas_wanted": "1",
    "gas_used": "0",
    "events": [
      {
        "type": "app",
        "attributes": [
          {
            "key": "YWN0aW9u",
            "value": "c2VuZA==",
            "index": false
          }
        ]
      }
    ],
    "codespace": "bank"
  },
  "id": 0,
  "jsonrpc": "2.0"
}                      
```
{% endcode %}
