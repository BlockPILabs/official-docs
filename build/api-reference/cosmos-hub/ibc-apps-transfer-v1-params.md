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
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/apps/transfer/v1/params

// Result
{
    "params": {
        "send_enabled": true,
        "receive_enabled": true
    }
}
```
{% endcode %}
