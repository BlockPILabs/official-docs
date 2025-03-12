---
description: Queries a nodeAccount by index.
---

# /zeta-chain/crosschain/nodeAccount{index}

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/nodeAccount/zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9

// Result
{
  "NodeAccount": {
    "creator": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
    "index": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
    "nodeAddress": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
    "pubkeySet": {
      "secp256k1": "zetapub1addwnpepq0y4zjwqd7aljxme8d5w3wpuelyj55jxhmn6h0u7y695esll6ragyvyanvl",
      "ed25519": ""
    },
    "nodeStatus": "Unknown"
  }
}
```
{% endcode %}
