---
description: >-
  Get info about the application.  Upon success, the Cache-Control header will
  be set with the default maximum age.
---

# /abci\_info

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/abci_info

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "response": {
            "data": "GaiaApp",
            "version": "v8.0.0",
            "last_block_height": "14184943",
            "last_block_app_hash": "HdOu+mu1LhUl2yy2lDfSPF5xOXqlpwOP5/e5MyFNX94="
        }
    }
}                   
```
{% endcode %}
