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
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/validators/cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn/slashes

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
