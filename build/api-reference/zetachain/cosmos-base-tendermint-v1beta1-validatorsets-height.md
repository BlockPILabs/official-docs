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
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/base/tendermint/v1beta1/validatorsets/2053715

// Result
{
    "block_height": "2053715",
    "validators": [
        {
            "address": "zetavalcons1pnnh5ejzy6fpsh6wuld0cgfd9g3ffwawdc7l0h",
            "pub_key": {
                "@type": "/cosmos.crypto.ed25519.PubKey",
                "key": "IYYt/r5YgdxYhwPWivBOgfGGBXMtd2ChQ8qv5RWqhvI="
            },
            "voting_power": "5000001000000",
            "proposer_priority": "3391819423641"
        },
        ......
        {
            "address": "zetavalcons195n5lay8qdpn534dd7kkxmsrg7m6mslc30aujp",
            "pub_key": {
                "@type": "/cosmos.crypto.ed25519.PubKey",
                "key": "U9b5SFkZ2XzhcsR5RHSTbJg6+RzaA90g0j/lWyt8STw="
            },
            "voting_power": "3",
            "proposer_priority": "-18749995126936"
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "6"
    }
}
```
{% endcode %}
