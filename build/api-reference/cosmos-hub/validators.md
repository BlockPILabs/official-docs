---
description: >-
  Get Validators. Validators are sorted by voting power.  If the height field is
  set to a non-default value, upon success, the Cache-Control header will be set
  with the default maximum age.
---

# /validators

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch information regarding the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/validators?height=14183822

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "block_height": "14183822",
        "validators": [
            {
                "address": "AC2D56057CD84765E6FBE318979093E8E44AA18F",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI="
                },
                "voting_power": "12376358",
                "proposer_priority": "68055808"
            },
            ......
        ],
        "count": "30",
        "total": "175"
    }
}
```
{% endcode %}
