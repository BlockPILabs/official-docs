---
description: Balance queries the balance of a single coin for a single account.
---

# /cosmos/bank/v1beta1/balances/{address}/by\_denom

#### **Parameters:**

**address-string,** address is the address to query balances for.

**denom-string,** denom is the coin denom to query balances for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/balances/zeta1qqqqy2e5k7vpgfam6d8fw9k9g04t06ccf56na8/by_denom?denom=azeta

// Result
{
    "balance": {
        "denom": "azeta",
        "amount": "100000000000000000"
    }
}
```
{% endcode %}
