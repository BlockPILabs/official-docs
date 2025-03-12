---
description: ValidatorDelegations queries delegate info for given validator.
---

# /cosmos/staking/v1beta1/validators/{validator\_addr}/delegations

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/zetavaloper1pptfhnyj37qn0nfuhmu7m5ssy5x6td8hmccpzl/delegations

// Result
{
  "delegation_responses": [
    {"delegation":{"delegator_address":"zeta1pptfhnyj37qn0nfuhmu7m5ssy5x6td8hlcqa0f","validator_address":"zetavaloper1pptfhnyj37qn0nfuhmu7m5ssy5x6td8hmccpzl","shares":"1000000000000000000000.000000000000000000"},"balance":{"denom":"azeta","amount":"990000000000000000000"}}
  ],
  "pagination": {
    "next_key": null,
    "total": "1"
  }
}
```
{% endcode %}
