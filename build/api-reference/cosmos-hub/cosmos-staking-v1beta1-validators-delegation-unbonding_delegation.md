---
description: UnbondingDelegation queries unbonding info for given validator delegator pair.
---

# /cosmos/staking/v1beta1/validators/{}/delegation/{}/unbonding\_delegation

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p/delegations/cosmos1rwacecm06qaleed52sszajandyenjkdf0c6n6c/unbonding_delegation

// Result
{
    "unbond": {
        "delegator_address": "cosmos1rwacecm06qaleed52sszajandyenjkdf0c6n6c",
        "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
        "entries": [
            {
                "creation_height": "13811912",
                "completion_time": "2023-02-15T11:03:01.397405310Z",
                "initial_balance": "35000000",
                "balance": "35000000"
            }
        ]
    }
}
```
{% endcode %}
