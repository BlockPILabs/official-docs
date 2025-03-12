---
description: ValidatorCommission queries accumulated commission for a validator.
---

# /cosmos/distribution/v1beta1/validators/{validator\_address}/commission

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r/commission

// Result
{
  "commission": {
    "commission": [
      {
        "denom": "azeta",
        "amount": "988859394858786621895066206426.914772182732964623"
      }
    ]
  }
}
```
{% endcode %}
