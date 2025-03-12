---
description: GetValidatorSetByHeight queries validator-set at a given height.
---

# /cosmos/base/tendermint/v1beta1/validatorsets/{height}

#### **Parameters:**

**height-string,** block height

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/base/tendermint/v1beta1/validatorsets/14063031

// Result
{
    "block_height": "14063031",
    "validators": [
        {
            "address": "cosmosvalcons14sk4vptumprktehmuvvf0yynarjy4gv08t64t4",
            "pub_key": {
                "@type": "/cosmos.crypto.ed25519.PubKey",
                "key": "0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI="
            },
            "voting_power": "12501342",
            "proposer_priority": "90518827"
        },
        ......
        {
            "address": "cosmosvalcons1lrjsx2uc6hfjgshrykmfwz6rfa6juyf7gszn2c",
            "pub_key": {
                "@type": "/cosmos.crypto.ed25519.PubKey",
                "key": "XN2+6Dh/5bCBWyk2ytv0ecSX+Hi9jdNxAYG70xHuqqw="
            },
            "voting_power": "222327",
            "proposer_priority": "-87213602"
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "175"
    }
}
```
{% endcode %}
