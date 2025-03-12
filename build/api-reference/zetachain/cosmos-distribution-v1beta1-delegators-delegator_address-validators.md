---
description: DelegatorValidators queries the validators of a delegator.
---

# /cosmos/distribution/v1beta1/delegators/{delegator\_address}/validators

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv/validators

// Result
{
  "validators": [
    "zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r"
  ]
}
```
{% endcode %}
