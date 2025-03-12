---
description: DelegatorDelegations queries all delegations of a given delegator address.
---

# /cosmos/staking/v1beta1/delegations/{delegator\_addr}

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegations/zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv

// Result
{
  "delegation_responses": [
    {
      "delegation": {
        "delegator_address": "zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv",
        "validator_address": "zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r",
        "shares": "100001000000000000002674.000000000000000000"
      },
      "balance": {
        "denom": "azeta",
        "amount": "100001000000000000002674"
      }
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "1"
  }
}
```
{% endcode %}
