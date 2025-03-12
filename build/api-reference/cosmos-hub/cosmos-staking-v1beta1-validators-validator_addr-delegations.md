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
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/cosmosvaloper1qphf0ferqcch0jca9hlqfm3x0eds3dpkcvpafp/delegations

// Result
{
    "delegation_responses": [
        {
            "delegation": {
                "delegator_address": "cosmos1qp9dxyv4e4gf4zmtrrgemsmuafehcl00screyr",
                "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
                "shares": "22300000.000000000000000000"
            },
            "balance": {
                "denom": "uatom",
                "amount": "22300000"
            }
        },
        {
            "delegation": {
                "delegator_address": "cosmos1qp6n9kdn2ywjrtp8gamypezlgllqqa4lcuv36r",
                "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
                "shares": "1000000.000000000000000000"
            },
            "balance": {
                "denom": "uatom",
                "amount": "1000000"
            }
        },
        ......
    ],
    "pagination": {
        "next_key": "FBiDVP7umU5sKgtD2sHyvCIAr7qLFLKaXLSsQnllbofqmneAvNA/K16s",
        "total": "1046"
    }
}
```
{% endcode %}
