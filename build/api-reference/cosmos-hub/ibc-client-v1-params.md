---
description: ClientParams queries all parameters of the ibc client.
---

# /ibc/client/v1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/cosmos/base/tendermint/v1beta1/blocks/latest

// Result
{
    "account": {
        "@type": "/cosmos.auth.v1beta1.BaseAccount",
        "address": "cosmos1hkthq04278pj5cqt7tsle4shs2hhlee4s9vc2m",
        "pub_key": {
            "@type": "/cosmos.crypto.secp256k1.PubKey",
            "key": "AiXtsRQ92h0CHiDnm7zVzX5weBvBHZDd/vcsTgzQ2d/e"
        },
        "account_number": "18666",
        "sequence": "387"
    }
}
```
{% endcode %}
