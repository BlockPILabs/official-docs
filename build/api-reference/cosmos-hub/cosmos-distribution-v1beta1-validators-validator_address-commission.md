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
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/validators/cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn/commission

// Result
{
    "commission": {
        "commission": [
            {
                "denom": "ibc/B05539B66B72E2739B986B86391E5D08F12B8D5D2C2A7F8F8CF9ADF674DFA231",
                "amount": "0.547514821986373833"
            },
            {
                "denom": "ibc/DEC41A02E47658D40FC71E5A35A9C807111F5A6662A3FB5DA84C4E6F53E616B3",
                "amount": "0.644107325848382482"
            },
            {
                "denom": "uatom",
                "amount": "212113563.782759871475859869"
            }
        ]
    }
}
```
{% endcode %}
