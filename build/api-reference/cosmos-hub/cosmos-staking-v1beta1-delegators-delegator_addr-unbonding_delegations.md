---
description: >-
  DelegatorUnbondingDelegations queries all unbonding delegations of a given
  delegator address.
---

# /cosmos/staking/v1beta1/delegators/{delegator\_addr}/unbonding\_delegations

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/unbonding_delegations

// Result
{
    "unbonding_responses": [],
    "pagination": {
        "next_key": null,
        "total": "0"
    }
}
```
{% endcode %}
