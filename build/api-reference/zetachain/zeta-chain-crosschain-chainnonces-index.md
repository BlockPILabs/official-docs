---
description: Queries a chainNonces by index.
---

# /zeta-chain/crosschain/chainNonces/{index}

#### **Parameters:**

**index - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/chainNonces/BAOBAB

// Result
{
    "ChainNonces": {
        "creator": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "index": "BAOBAB",
        "chain": "BAOBAB",
        "nonce": "103",
        "signers": [
            "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
            "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
            "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9"
        ],
        "finalizedHeight": "0"
    }
}
```
{% endcode %}
