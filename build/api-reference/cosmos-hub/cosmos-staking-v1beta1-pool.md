---
description: Pool queries the pool info.
---

# /cosmos/staking/v1beta1/pool

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/pool

// Result
{
    "pool": {
        "not_bonded_tokens": "6041984437357",
        "bonded_tokens": "207384995638960"
    }
}
```
{% endcode %}
