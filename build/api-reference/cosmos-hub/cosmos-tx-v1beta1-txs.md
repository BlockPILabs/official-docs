---
description: GetTxsEvent fetches txs by event.
---

# /cosmos/tx/v1beta1/txs

#### **Parameters:**

**query - array\[string]**, query is the list of transaction event type.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/tx/v1beta1/txs?query=message.sender=%27cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9%27

// Result
{
    "txs": [
        {
            "body": {
                "messages": [
                    {
                        "@type": "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
                        "delegator_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9",
                        "validator_address": "cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq"
                    },
                    {
                        "@type": "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
                        "delegator_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9",
                        "validator_address": "cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf"
                    },
                    {
                        "@type": "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
                        "delegator_address": "cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9",
                        "validator_address": "cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn"
                    }
                ],
                "memo": "",
                "timeout_height": "0",
                "extension_options": [],
                "non_critical_extension_options": []
            },
            "auth_info": {
                "signer_infos": [
                    {
                        "public_key": {
                            "@type": "/cosmos.crypto.secp256k1.PubKey",
                            "key": "AoECxjesvkS7x/qxQHYriMAJkMaDhxrb4ItoLo7AwRuK"
                        },
                        "mode_info": {
                            "single": {
                                "mode": "SIGN_MODE_LEGACY_AMINO_JSON"
                            }
                        },
                        "sequence": "65"
                    }
                ],
                "fee": {
                    "amount": [
                        {
                            "denom": "uatom",
                            "amount": "11819"
                        }
                    ],
                    "gas_limit": "472746",
                    "payer": "",
                    "granter": ""
                }
            },
            "signatures": [
                "oHFb/JytyyZ2nailPbOHEZg+yCyb7olEyBQXkXTVhoY+O/Y2Pzl760MWxo3knh4Fbe7ZQLRKmERlnBkEgUq++w=="
            ]
        },
        ......
    ],
    "pagination": {
        "next_key": null,
        "total": "2"
    }
}  
```
{% endcode %}
