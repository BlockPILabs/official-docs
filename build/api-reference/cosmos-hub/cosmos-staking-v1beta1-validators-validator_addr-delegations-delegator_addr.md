---
description: Delegation queries delegate info for given validator delegator pair.
---

# /cosmos/staking/v1beta1/validators/{validator\_addr}/delegations/{delegator\_addr}

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p/delegations/cosmos1z74ey263de7x2vq76h7kjd5qn5nk80tyca20zg

// Result
{
    "delegation_response": {
        "delegation": {
            "delegator_address": "cosmos1z74ey263de7x2vq76h7kjd5qn5nk80tyca20zg",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "shares": "258232.000000000000000000"
        },
        "balance": {
            "denom": "uatom",
            "amount": "258232"
        }
    }
}
```
{% endcode %}
