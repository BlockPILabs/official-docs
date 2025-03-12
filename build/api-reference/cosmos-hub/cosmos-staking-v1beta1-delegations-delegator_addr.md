---
description: DelegatorDelegations queries all delegations of a given delegator address.
---

# /cosmos/staking/v1beta1/delegations/{delegator\_addr}

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegations/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9

// Result
{
    "delegation_responses": [
        {
            "delegation": {
                "delegator_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9",
                "validator_address": "cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf",
                "shares": "25002500.226916793412571107"
            },
            "balance": {
                "denom": "uatom",
                "amount": "25000000"
            }
        },
        {
            "delegation": {
                "delegator_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9",
                "validator_address": "cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq",
                "shares": "25000000.000000000000000000"
            },
            "balance": {
                "denom": "uatom",
                "amount": "25000000"
            }
        },
        {
            "delegation": {
                "delegator_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9",
                "validator_address": "cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn",
                "shares": "22000000.000000000000000000"
            },
            "balance": {
                "denom": "uatom",
                "amount": "22000000"
            }
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "3"
    }
}
```
{% endcode %}
