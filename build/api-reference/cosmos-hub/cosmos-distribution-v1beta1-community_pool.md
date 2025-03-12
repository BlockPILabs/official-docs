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
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/distribution/v1beta1/community_pool

// Result
{
    "pool": [
        {
            "denom": "ibc/B05539B66B72E2739B986B86391E5D08F12B8D5D2C2A7F8F8CF9ADF674DFA231",
            "amount": "1723780.372440649688311864"
        },
        {
            "denom": "ibc/DEC41A02E47658D40FC71E5A35A9C807111F5A6662A3FB5DA84C4E6F53E616B3",
            "amount": "2117.757979823080461952"
        },
        {
            "denom": "uatom",
            "amount": "1544951808401.852262704391174176"
        }
    ]
}
```
{% endcode %}
