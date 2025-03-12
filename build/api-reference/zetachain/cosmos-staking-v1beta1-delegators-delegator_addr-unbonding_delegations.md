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
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegators/zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv/unbonding_delegations

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
