---
description: Params queries params of the distribution module.
---

# /cosmos/distribution/v1beta1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/params

// Result
{
  "params": {
    "community_tax": "0.020000000000000000",
    "base_proposer_reward": "0.010000000000000000",
    "bonus_proposer_reward": "0.040000000000000000",
    "withdraw_addr_enabled": true
  }
}
```
{% endcode %}
