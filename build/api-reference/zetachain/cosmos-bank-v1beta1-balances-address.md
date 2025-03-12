---
description: AllBalances queries the balance of all coins for a single account.
---

# /cosmos/bank/v1beta1/balances/{address}

#### **Parameters:**

**address-string,** address is the address to query balances for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/balances/zeta1qqqqy2e5k7vpgfam6d8fw9k9g04t06ccf56na8

// Result
{
  "balances": [
    {
      "denom": "azeta",
      "amount": "100000000000000000"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "1"
  }
}
```
{% endcode %}
