---
description: ModuleAccounts returns all the existing module accounts.
---

# /cosmos/auth/v1beta1/module\_accounts

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/module_accounts

// Result
{
  "accounts": [
    {
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
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1ku7q4tzvresxcmjftkzgr934tektxqup3wvnad",
        "pub_key": null,
        "account_number": "64",
        "sequence": "0"
      },
      "name": "crosschain",
      "permissions": [
        "minter",
        "burner"
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1jv65s3grqf6v6jl3dp4t6c9t9rk99cd83m2fn0",
        "pub_key": null,
        "account_number": "35",
        "sequence": "0"
      },
      "name": "distribution",
      "permissions": [
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1w43fn2ze2wyhu5hfmegr6vp52c3dgn0srdgymy",
        "pub_key": null,
        "account_number": "40",
        "sequence": "0"
      },
      "name": "emissions",
      "permissions": [
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1pyks89mqljlpgzenwa0g8zch0hptk6usd9vcuh",
        "pub_key": null,
        "account_number": "42",
        "sequence": "0"
      },
      "name": "emissionsObservers",
      "permissions": [
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1v8v7zkyt7j3dc526k4alsu8vspvqqg342t27vu",
        "pub_key": null,
        "account_number": "41",
        "sequence": "0"
      },
      "name": "emissionsTss",
      "permissions": [
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1vqu8rska6swzdmnhf90zuv0xmelej4lqmktpwc",
        "pub_key": null,
        "account_number": "50",
        "sequence": "0"
      },
      "name": "evm",
      "permissions": [
        "minter",
        "burner"
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta17xpfvakm2amg962yls6f84z3kell8c5lxad43d",
        "pub_key": null,
        "account_number": "34",
        "sequence": "0"
      },
      "name": "fee_collector",
      "permissions": [
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1wdd3fwmegces02ktakrd4uej9v0xyf4trw8fja",
        "pub_key": null,
        "account_number": "39",
        "sequence": "9"
      },
      "name": "fungible",
      "permissions": [
        "minter",
        "burner"
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta10d07y265gmmuvt4z0w9aw880jnsr700jvxasvr",
        "pub_key": null,
        "account_number": "38",
        "sequence": "0"
      },
      "name": "gov",
      "permissions": [
        "burner"
      ]
    },
    {
      "@type": "/cosmos.auth.v1beta1.ModuleAccount",
      "base_account": {
        "address": "zeta1tygms3xhhs3yv487phx3dw4a95jn7t7lhlmt4n",
        "pub_key": null,
        "account_number": "37",
        "sequence": "0"
      },
      "name": "not_bonded_tokens_pool",
      "permissions": [
        "burner",
        "staking"
      ]
    }
  ]
}
```
{% endcode %}
