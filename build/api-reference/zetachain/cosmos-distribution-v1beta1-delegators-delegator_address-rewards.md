---
description: DelegationTotalRewards queries the total rewards accrued by a each validator.
---

# /cosmos/distribution/v1beta1/delegators/{delegator\_address}/rewards

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv/rewards

// Result
{
  "rewards": [
    {
      "validator_address": "zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r",
      "reward": [
        {
          "denom": "azeta",
          "amount": "190001687479927365986376652732.270085065489201710"
        }
      ]
    }
  ],
  "total": [
    {
      "denom": "azeta",
      "amount": "190001687479927365986376652732.270085065489201710"
    }
  ]
}
```
{% endcode %}
