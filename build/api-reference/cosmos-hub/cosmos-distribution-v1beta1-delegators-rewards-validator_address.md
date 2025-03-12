---
description: DelegationRewards queries the total rewards accrued by a delegation.
---

# /cosmos/distribution/v1beta1/delegators/{}/rewards/{validator\_address}

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/rewards/cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn

// Result
{
    "rewards": [
        {
            "denom": "uatom",
            "amount": "13180.282707075550000000"
        }
    ]
}
```
{% endcode %}
