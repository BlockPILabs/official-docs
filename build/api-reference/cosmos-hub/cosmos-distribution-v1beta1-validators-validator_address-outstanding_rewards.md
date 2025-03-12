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
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/validators/cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn/outstanding_rewards

// Result
{
    "rewards": {
        "rewards": [
            {
                "denom": "ibc/B05539B66B72E2739B986B86391E5D08F12B8D5D2C2A7F8F8CF9ADF674DFA231",
                "amount": "39820.770444012720578677"
            },
            {
                "denom": "ibc/DEC41A02E47658D40FC71E5A35A9C807111F5A6662A3FB5DA84C4E6F53E616B3",
                "amount": "59.166770188234847667"
            },
            {
                "denom": "uatom",
                "amount": "132355578945.832304244883531986"
            }
        ]
    }
}
```
{% endcode %}
