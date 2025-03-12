---
description: DelegatorValidators queries the validators of a delegator.
---

# /cosmos/distribution/v1beta1/delegators/{delegator\_address}/validators

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/validators

// Result
{
    "validators": [
        "cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf",
        "cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq",
        "cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn"
    ]
}
```
{% endcode %}
