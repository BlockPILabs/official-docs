---
description: Accounts returns all the existing accounts
---

# /cosmos/auth/v1beta1/accounts

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/accounts

// Result
{
  "accounts": [
    {
      "@type": "/ethermint.types.v1.EthAccount",
      "base_account": {
        "address": "zeta1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqy2dvvjh",
        "pub_key": null,
        "account_number": "11088",
        "sequence": "0"
      },
      "code_hash": "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
    },
    ......
  ],
  "pagination": {
    "next_key": "AXfhspChrPgHp04aT49tY5YbroE=",
    "total": "11171"
  }
}
```
{% endcode %}
