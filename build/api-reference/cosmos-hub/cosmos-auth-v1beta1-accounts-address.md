---
description: Account returns account details based on address.
---

# /cosmos/auth/v1beta1/accounts/{address}

#### **Parameters:**

**address-string**，address defines the address to query for

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/accounts/cosmos1hkthq04278pj5cqt7tsle4shs2hhlee4s9vc2m

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
