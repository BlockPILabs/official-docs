---
description: ModuleVersions queries the list of module versions from state.
---

# /cosmos/upgrade/v1beta1/module\_versions

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/upgrade/v1beta1/module_versions

// Result
{
  "module_versions": [
    {
      "name": "auth",
      "version": "2"
    },
    {
      "name": "bank",
      "version": "2"
    },
    {
      "name": "capability",
      "version": "1"
    },
    {
      "name": "crisis",
      "version": "1"
    },
    {
      "name": "crosschain",
      "version": "1"
    },
    {
      "name": "distribution",
      "version": "2"
    },
    {
      "name": "evidence",
      "version": "1"
    },
    {
      "name": "evm",
      "version": "3"
    },
    {
      "name": "feemarket",
      "version": "3"
    },
    {
      "name": "fungible",
      "version": "2"
    },
    {
      "name": "genutil",
      "version": "1"
    },
    {
      "name": "gov",
      "version": "2"
    },
    {
      "name": "ibc",
      "version": "2"
    },
    {
      "name": "mint",
      "version": "1"
    },
    {
      "name": "observer",
      "version": "1"
    },
    {
      "name": "params",
      "version": "1"
    },
    {
      "name": "slashing",
      "version": "2"
    },
    {
      "name": "staking",
      "version": "2"
    },
    {
      "name": "transfer",
      "version": "2"
    },
    {
      "name": "upgrade",
      "version": "1"
    },
    {
      "name": "vesting",
      "version": "1"
    }
  ]
}
```
{% endcode %}
