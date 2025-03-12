---
description: ValidatorOutstandingRewards queries rewards of a validator address.
---

# /cosmos/distribution/v1beta1/validators/{validator\_address}/outstanding\_rewards

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r/outstanding_rewards

// Result
{
  "rewards": {
    "rewards": [
      {
        "denom": "azeta",
        "amount": "9888593866617261659997121712235.259593725686243710"
      }
    ]
  }
}
```
{% endcode %}
