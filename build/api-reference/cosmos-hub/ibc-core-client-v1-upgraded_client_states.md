---
description: UpgradedClientState queries an Upgraded IBC light client.
---

# /ibc/core/client/v1/upgraded\_client\_states

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/client/v1/upgraded_client_states

// Result
{
    "code": 5,
    "message": "rpc error: code = NotFound desc = light client not found: key not found",
    "details": []
}
```
{% endcode %}
