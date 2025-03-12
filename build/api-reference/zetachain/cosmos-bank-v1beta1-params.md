---
description: Params queries the parameters of x/bank module.
---

# /cosmos/bank/v1beta1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/params

// Result
{
    "params": {
        "send_enabled": [],
        "default_send_enabled": true
    }
}
```
{% endcode %}
