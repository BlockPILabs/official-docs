---
description: DelegatorWithdrawAddress queries withdraw address of a delegator.
---

# /cosmos/distribution/v1beta1/delegators/{delegator\_address}/withdraw\_address

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/withdraw_address

// Result
{
    "withdraw_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9"
}
```
{% endcode %}
