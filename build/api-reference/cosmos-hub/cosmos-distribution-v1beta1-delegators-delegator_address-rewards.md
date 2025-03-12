---
description: DelegationTotalRewards queries the total rewards accrued by a each validator.
---

# /cosmos/distribution/v1beta1/delegators/{delegator\_address}/rewards

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
````json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/rewards

// Result
```json
{
    "rewards": [
        {
            "validator_address": "cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf",
            "reward": [
                {
                    "denom": "uatom",
                    "amount": "15578.304811743226558942"
                }
            ]
        },
        {
            "validator_address": "cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq",
            "reward": [
                {
                    "denom": "uatom",
                    "amount": "15575.309255530325000000"
                }
            ]
        },
        {
            "validator_address": "cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn",
            "reward": [
                {
                    "denom": "uatom",
                    "amount": "13144.557599246568000000"
                }
            ]
        }
    ],
    "total": [
        {
            "denom": "uatom",
            "amount": "44298.171666520119558942"
        }
    ]
}
```
````
{% endcode %}
