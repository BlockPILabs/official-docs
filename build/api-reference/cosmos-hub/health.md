---
description: >-
  Get node health. Returns empty result (200 OK) on success, no response - in
  case of an error.
---

# /health

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/health

// Result
{
  "jsonrpc": "2.0",
  "id": -1,
  "result": {}
}
```
{% endcode %}
