---
description: >-
  SpendableBalances queries the spenable balance of all coins for a single
  account.
---

# /cosmos/bank/v1beta1/spendable\_balances/{address}

#### **Parameters:**

**address-string**, address is the address to query spendable balances for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/spendable_balances/zeta1qqqq7hq2neye0l0ar64q2ry0ggch94c0pxj67c

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
