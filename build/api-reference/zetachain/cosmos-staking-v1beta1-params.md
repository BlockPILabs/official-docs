---
description: Parameters queries the staking parameters.
---

# /cosmos/staking/v1beta1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/params

// Result
{
  "params": {
    "unbonding_time": "300s",
    "max_validators": 100,
    "max_entries": 7,
    "historical_entries": 10000,
    "bond_denom": "azeta"
  }
}
```
{% endcode %}
