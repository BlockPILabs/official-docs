---
description: SupplyOf queries the supply of a single coin.
---

# /cosmos/bank/v1beta1/supply/by\_denom

#### **Parameters:**

**denom-string,** denom is the coin denom to query balances for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/supply/by_denom/uatom

// Result
{
    "amount": {
        "denom": "atom",
        "amount": "0"
    }
}
```
{% endcode %}
