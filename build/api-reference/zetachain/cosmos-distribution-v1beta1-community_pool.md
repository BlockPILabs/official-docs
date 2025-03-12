---
description: CommunityPool queries the community pool coins.
---

# /cosmos/distribution/v1beta1/community\_pool

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/community_pool

// Result
{
    "pool": [
        {
            "denom": "azeta",
            "amount": "130976519097831776212463039694846.441903727284595188"
        }
    ]
}
```
{% endcode %}
