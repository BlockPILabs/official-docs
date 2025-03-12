---
description: Query the application for some information.
---

# /abci\_query

#### **Parameters:**

**path - string**, Path to the data ("/a/b/c")

**data- string**, Data

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/abci_query?path=%22/app/version%22&data&height=14183822&prove=true

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "response": {
            "code": 6,
            "log": "no query path provided: unknown request",
            "info": "",
            "index": "0",
            "key": null,
            "value": null,
            "proofOps": null,
            "height": "0",
            "codespace": "sdk"
        }
    }
}              
```
{% endcode %}
