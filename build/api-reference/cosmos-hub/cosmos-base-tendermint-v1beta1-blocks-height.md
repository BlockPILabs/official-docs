---
description: GetBlockByHeight queries block for given height.
---

# /cosmos/base/tendermint/v1beta1/blocks/{height}

#### **Parameters:**

**height-string,** block height

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/base/tendermint/v1beta1/blocks/14063031

// Result
{
    "block_id": {
        "hash": "wrEgUu1TcEQcgQ23nA/yjO62zMEFzuFiXQzZ9hCnsbM=",
        "part_set_header": {
            "total": 1,
            "hash": "YYBTPolyEdZfHuEXxYUSEM+bh/w0CvBVGl2CG1DbnSI="
        }
    },
    "block": {
        ......
    }
}
```
{% endcode %}
