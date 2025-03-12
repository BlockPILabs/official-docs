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
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/client/v1/upgraded_client_states

// Result
{
    "code": 5,
    "message": "rpc error: code = NotFound desc = light client not found: key not found",
    "details": []
}
```
{% endcode %}
