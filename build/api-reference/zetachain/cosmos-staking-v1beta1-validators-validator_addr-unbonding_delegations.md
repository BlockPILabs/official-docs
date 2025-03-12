---
description: /cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations
---

# /cosmos/staking/v1beta1/validators/{validator\_addr}/unbonding\_delegations

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r/unbonding_delegations

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
