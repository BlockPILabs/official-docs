---
description: Params queries all parameters of the ibc-transfer module.
---

# /ibc/apps/transfer/v1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/apps/transfer/v1/params

// Result
{
    "params": {
        "send_enabled": true,
        "receive_enabled": true
    }
}
```
{% endcode %}
