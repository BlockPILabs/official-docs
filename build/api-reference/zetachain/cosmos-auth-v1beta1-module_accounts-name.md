---
description: ModuleAccountByName returns the module account info by module name
---

# /cosmos/auth/v1beta1/module\_accounts/{name}

#### **Parameters:**

**name-string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/module_accounts/bonded_tokens_pool

// Result
{
  "account": {
    "@type": "/cosmos.auth.v1beta1.ModuleAccount",
    "base_account": {
      "address": "zeta1fl48vsnmsdzcv85q5d2q4z5ajdha8yu3rl86r8",
      "pub_key": null,
      "account_number": "36",
      "sequence": "0"
    },
    "name": "bonded_tokens_pool",
    "permissions": [
      "burner",
      "staking"
    ]
  }
}
```
{% endcode %}
