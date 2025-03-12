---
description: ValidatorSlashes queries slash events of a validator.
---

# /cosmos/distribution/v1beta1/validators/{validator\_address}/slashes

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r/slashes

// Result
{
  "slashes": [],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
```
{% endcode %}
