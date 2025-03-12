---
description: >-
  Search for blocks by BeginBlock and EndBlock events.  See /subscribe for the
  query syntax.
---

# /block\_search

#### **Parameters:**

**query - string**, Query

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/block_search?query=%22block.height%3D2115661%22

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "blocks": [],
        "total_count": "0"
    }
}                 
```
{% endcode %}
