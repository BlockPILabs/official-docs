---
description: Get the latest validator set
---

# /validatorsets/latest

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/validatorsets/latest

// Result
{
    "height": "0",
    "result": {
        "block_height": "14090671",
        "validators": [
            {
                "address": "cosmosvalcons14sk4vptumprktehmuvvf0yynarjy4gv08t64t4",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI="
                },
                "proposer_priority": "80801660",
                "voting_power": "12507660"
            },
            {
                "address": "cosmosvalcons1yxv746y5egu3l2p0q8pvv99lavgr6ptvdhx306",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "C+VWc34ZF6n/QoIAXo4191OwKxQWpbFnrGKCqcNbe1E="
                },
                "proposer_priority": "-50536031",
                "voting_power": "10480094"
            },
            ......
        ],
        "total": "175"
    }
}
```
{% endcode %}
