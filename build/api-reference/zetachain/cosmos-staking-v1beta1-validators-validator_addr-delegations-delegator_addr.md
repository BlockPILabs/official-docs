---
description: Delegation queries delegate info for given validator delegator pair.
---

# /cosmos/staking/v1beta1/validators/{validator\_addr}/delegations/{delegator\_addr}

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r/delegations/zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84

// Result
{
  "delegation_response": {
    "delegation": {
      "delegator_address": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "validator_address": "zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r",
      "shares": "1000000000000000000000000.000000000000000000"
    },
    "balance": {
      "denom": "azeta",
      "amount": "1000000000000000000000000"
    }
  }
}
```
{% endcode %}
