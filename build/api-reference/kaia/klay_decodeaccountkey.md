---
description: Decodes an RLP encoded account key.
---

# kaia\_decodeAccountKey

#### **Parameters**

| Type | Description             |
| ---- | ----------------------- |
| DATA | RLP encoded account key |

#### **Return Value**

| Name    | Type      |                                            |
| ------- | --------- | ------------------------------------------ |
| keytype | QUANTITY  | Integer value indicating account key type. |
| key     | JSON DATA | Account key object                         |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "kaia_decodeAccountKey", "params": ["0x05f898a302a103e4a01407460c1c03ac0c82fd84f303a699b210c0b054f4aff72ff7dcdf01512db84e04f84b02f848e301a103e4a01407460c1c03ac0c82fd84f303a699b210c0b054f4aff72ff7dcdf01512de301a10336f6355f5b532c3c1606f18fa2be7a16ae200c5159c8031dd25bfa389a4c9c06a302a102c8785266510368d9372badd4c7f4a94b692e82ba74e0b5e26b34558b0f081447"], "id": 47}' http://klaytn.testnet.blockpi.net/v1/rpc/your-api-key

// Result
{
    "id": 47,
    "jsonrpc": "2.0",
    "result": {
        "key": [
            {
                "key": {
                    "x": "0xe4a01407460c1c03ac0c82fd84f303a699b210c0b054f4aff72ff7dcdf01512d",
                    "y": "0xa5735a23ce1654b14680054a993441eae7c261983a56f8e0da61280758b5919"
                },
                "keyType": 2
            },
            {
                "key": {
                    "keys": [
                        {
                            "key": {
                                "x": "0xe4a01407460c1c03ac0c82fd84f303a699b210c0b054f4aff72ff7dcdf01512d",
                                "y": "0xa5735a23ce1654b14680054a993441eae7c261983a56f8e0da61280758b5919"
                            },
                            "weight": 1
                        },
                        {
                            "key": {
                                "x": "0x36f6355f5b532c3c1606f18fa2be7a16ae200c5159c8031dd25bfa389a4c9c06",
                                "y": "0x6fdf9fc87a16ac359e66d9761445d5ccbb417fb7757a3f5209d713824596a50d"
                            },
                            "weight": 1
                        }
                    ],
                    "threshold": 2
                },
                "keyType": 4
            },
            {
                "key": {
                    "x": "0xc8785266510368d9372badd4c7f4a94b692e82ba74e0b5e26b34558b0f081447",
                    "y": "0x94c27901465af0a703859ab47f8ae17e54aaba453b7cde5a6a9e4a32d45d72b2"
                },
                "keyType": 2
            }
        ],
        "keyType": 5
    }
}
```
{% endcode %}
