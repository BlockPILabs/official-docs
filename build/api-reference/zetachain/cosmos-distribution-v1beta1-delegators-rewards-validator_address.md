---
description: DelegationRewards queries the total rewards accrued by a delegation.
---

# /cosmos/distribution/v1beta1/delegators/{}/rewards/{validator\_address}

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv/rewards/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r

// Result
{
  "rewards": [
    {
      "denom": "azeta",
      "amount": "190001689003542682674558826526.011151223069617232"
    }
  ]
}
```
{% endcode %}
