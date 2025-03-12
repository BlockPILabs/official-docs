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
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/abci_info

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "response": {
            "data": "zetacore",
            "version": "athens2-v1.1.10",
            "last_block_height": "2116638",
            "last_block_app_hash": "EUHYYalWQV1VPg1N/apOdx//nWE7g+mR0i0YAzDeRPc="
        }
    }
}               
```
{% endcode %}
