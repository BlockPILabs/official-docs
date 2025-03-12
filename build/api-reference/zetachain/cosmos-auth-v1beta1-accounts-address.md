---
description: Account returns account details based on address.
---

# /cosmos/auth/v1beta1/accounts/{address}

#### **Parameters:**

**address-string**，address defines the address to query for

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/accounts/zeta1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqy2dvvjh

// Result
{
  "account": {
    "@type": "/ethermint.types.v1.EthAccount",
    "base_account": {
      "address": "zeta1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqy2dvvjh",
      "pub_key": null,
      "account_number": "11088",
      "sequence": "0"
    },
    "code_hash": "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
  }
}
```
{% endcode %}
