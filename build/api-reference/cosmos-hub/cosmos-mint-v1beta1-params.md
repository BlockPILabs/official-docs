---
description: Params returns the total set of minting parameters.
---

# /cosmos/mint/v1beta1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/mint/v1beta1/params

// Result
{
    "params": {
        "mint_denom": "uatom",
        "inflation_rate_change": "1.000000000000000000",
        "inflation_max": "0.200000000000000000",
        "inflation_min": "0.070000000000000000",
        "goal_bonded": "0.670000000000000000",
        "blocks_per_year": "4360000"
    }
}
```
{% endcode %}
