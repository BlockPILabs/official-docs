---
description: Params queries the parameters of slashing module
---

# /cosmos/slashing/v1beta1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/slashing/v1beta1/params

// Result
{
    "params": {
        "signed_blocks_window": "10000",
        "min_signed_per_window": "0.050000000000000000",
        "downtime_jail_duration": "600s",
        "slash_fraction_double_sign": "0.050000000000000000",
        "slash_fraction_downtime": "0.000100000000000000"
    }
}
```
{% endcode %}
