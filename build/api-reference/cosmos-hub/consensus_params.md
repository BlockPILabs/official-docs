---
description: >-
  Get consensus parameters.  If the height field is set to a non-default value,
  upon success, the Cache-Control header will be set with the default maximum
  age.
---

# /consensus\_params

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch commit informations regarding the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/consensus_params?height=14184173

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "block_height": "14184276",
        "consensus_params": {
            "block": {
                "max_bytes": "200000",
                "max_gas": "40000000",
                "time_iota_ms": "1000"
            },
            "evidence": {
                "max_age_num_blocks": "1000000",
                "max_age_duration": "172800000000000",
                "max_bytes": "50000"
            },
            "validator": {
                "pub_key_types": [
                    "ed25519"
                ]
            },
            "version": {}
        }
    }
} 
```
{% endcode %}
