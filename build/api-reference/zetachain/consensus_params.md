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
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/consensus_params?height=14184173

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "block_height": "2116334",
        "consensus_params": {
            "block": {
                "max_bytes": "22020096",
                "max_gas": "500000000",
                "time_iota_ms": "1000"
            },
            "evidence": {
                "max_age_num_blocks": "100000",
                "max_age_duration": "172800000000000",
                "max_bytes": "1048576"
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
