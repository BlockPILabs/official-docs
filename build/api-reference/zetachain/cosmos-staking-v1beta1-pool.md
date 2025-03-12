---
description: Pool queries the pool info.
---

# /cosmos/staking/v1beta1/pool

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/pool

// Result
{
  "pool": {
    "not_bonded_tokens": "29370490928495197442",
    "bonded_tokens": "20000005100005972544000001002674"
  }
}
```
{% endcode %}
