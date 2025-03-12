---
description: GetTx fetches a tx by hash.
---

# /cosmos/tx/v1beta1/txs/{hash}

#### **Parameters:**

**hash - string**, hash is the tx hash to query, encoded as a hex string.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/tx/v1beta1/txs/11D97480C2B51923ADBCC52A5FB16C36EE3A0D6F54B9D600E688AF9EB68B7DBB

// Result
{
    "tx": {
        "body": {
            "messages": [
                {
                    "@type": "/cosmos.bank.v1beta1.MsgSend",
                    "from_address": "cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs",
                    "to_address": "cosmos1psr5x3kgra5fvm4gc4l6ufykn0nl3esdjeex8n",
                    "amount": [
                        {
                            "denom": "uatom",
                            "amount": "1480000"
                        }
                    ]
                }
            ],
            "memo": "1198953800",
            "timeout_height": "0",
            "extension_options": [],
            "non_critical_extension_options": []
        },
        "auth_info": {
            "signer_infos": [
                {
                    "public_key": {
                        "@type": "/cosmos.crypto.secp256k1.PubKey",
                        "key": "AmnGyavh0adrcPyd/u5tspwQWPZSJTc/u3mFR9k+ResD"
                    },
                    "mode_info": {
                        "single": {
                            "mode": "SIGN_MODE_DIRECT"
                        }
                    },
                    "sequence": "4"
                }
            ],
            "fee": {
                "amount": [
                    {
                        "denom": "uatom",
                        "amount": "1000"
                    }
                ],
                "gas_limit": "500000",
                "payer": "",
                "granter": ""
            }
        },
        "signatures": [
            "YIpJdDghDCNt/uBQi5QHG8AQEMjnjdXRypJvVkCEgPUzkJzTGtGCN5G18ubVWf0PXzS0brmBHfS4phcm4kGYUw=="
        ]
    },
    "tx_response": {
        "height": "14090525",
        "txhash": "11D97480C2B51923ADBCC52A5FB16C36EE3A0D6F54B9D600E688AF9EB68B7DBB",
        "codespace": "",
        "code": 0,
        "data": "0A1E0A1C2F636F736D6F732E62616E6B2E763162657461312E4D736753656E64",
        "raw_log": "[{\"events\":[{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"cosmos1psr5x3kgra5fvm4gc4l6ufykn0nl3esdjeex8n\"},{\"key\":\"amount\",\"value\":\"1480000uatom\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs\"},{\"key\":\"amount\",\"value\":\"1480000uatom\"}]},{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"/cosmos.bank.v1beta1.MsgSend\"},{\"key\":\"sender\",\"value\":\"cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs\"},{\"key\":\"module\",\"value\":\"bank\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"cosmos1psr5x3kgra5fvm4gc4l6ufykn0nl3esdjeex8n\"},{\"key\":\"sender\",\"value\":\"cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs\"},{\"key\":\"amount\",\"value\":\"1480000uatom\"}]}]}]",
        "logs": [
            {
                "msg_index": 0,
                "log": "",
                "events": [
                    {
                        "type": "coin_received",
                        "attributes": [
                            {
                                "key": "receiver",
                                "value": "cosmos1psr5x3kgra5fvm4gc4l6ufykn0nl3esdjeex8n"
                            },
                            {
                                "key": "amount",
                                "value": "1480000uatom"
                            }
                        ]
                    },
                    {
                        "type": "coin_spent",
                        "attributes": [
                            {
                                "key": "spender",
                                "value": "cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs"
                            },
                            {
                                "key": "amount",
                                "value": "1480000uatom"
                            }
                        ]
                    },
                    {
                        "type": "message",
                        "attributes": [
                            {
                                "key": "action",
                                "value": "/cosmos.bank.v1beta1.MsgSend"
                            },
                            {
                                "key": "sender",
                                "value": "cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs"
                            },
                            {
                                "key": "module",
                                "value": "bank"
                            }
                        ]
                    },
                    {
                        "type": "transfer",
                        "attributes": [
                            {
                                "key": "recipient",
                                "value": "cosmos1psr5x3kgra5fvm4gc4l6ufykn0nl3esdjeex8n"
                            },
                            {
                                "key": "sender",
                                "value": "cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs"
                            },
                            {
                                "key": "amount",
                                "value": "1480000uatom"
                            }
                        ]
                    }
                ]
            }
        ],
        "info": "",
        "gas_wanted": "500000",
        "gas_used": "67571",
        "tx": {
            "@type": "/cosmos.tx.v1beta1.Tx",
            "body": {
                "messages": [
                    {
                        "@type": "/cosmos.bank.v1beta1.MsgSend",
                        "from_address": "cosmos1a0d206nnylpxf8ta9kcrff5mucja7h228xwxqs",
                        "to_address": "cosmos1psr5x3kgra5fvm4gc4l6ufykn0nl3esdjeex8n",
                        "amount": [
                            {
                                "denom": "uatom",
                                "amount": "1480000"
                            }
                        ]
                    }
                ],
                "memo": "1198953800",
                "timeout_height": "0",
                "extension_options": [],
                "non_critical_extension_options": []
            },
            "auth_info": {
                "signer_infos": [
                    {
                        "public_key": {
                            "@type": "/cosmos.crypto.secp256k1.PubKey",
                            "key": "AmnGyavh0adrcPyd/u5tspwQWPZSJTc/u3mFR9k+ResD"
                        },
                        "mode_info": {
                            "single": {
                                "mode": "SIGN_MODE_DIRECT"
                            }
                        },
                        "sequence": "4"
                    }
                ],
                "fee": {
                    "amount": [
                        {
                            "denom": "uatom",
                            "amount": "1000"
                        }
                    ],
                    "gas_limit": "500000",
                    "payer": "",
                    "granter": ""
                }
            },
            "signatures": [
                "YIpJdDghDCNt/uBQi5QHG8AQEMjnjdXRypJvVkCEgPUzkJzTGtGCN5G18ubVWf0PXzS0brmBHfS4phcm4kGYUw=="
            ]
        },
        "timestamp": "2023-02-15T08:23:58Z",
        "events": [
            {
                "type": "coin_spent",
                "attributes": [
                    {
                        "key": "c3BlbmRlcg==",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    },
                    {
                        "key": "YW1vdW50",
                        "value": "MTAwMHVhdG9t",
                        "index": true
                    }
                ]
            },
            {
                "type": "coin_received",
                "attributes": [
                    {
                        "key": "cmVjZWl2ZXI=",
                        "value": "Y29zbW9zMTd4cGZ2YWttMmFtZzk2MnlsczZmODR6M2tlbGw4YzVsc2VycXRh",
                        "index": true
                    },
                    {
                        "key": "YW1vdW50",
                        "value": "MTAwMHVhdG9t",
                        "index": true
                    }
                ]
            },
            {
                "type": "transfer",
                "attributes": [
                    {
                        "key": "cmVjaXBpZW50",
                        "value": "Y29zbW9zMTd4cGZ2YWttMmFtZzk2MnlsczZmODR6M2tlbGw4YzVsc2VycXRh",
                        "index": true
                    },
                    {
                        "key": "c2VuZGVy",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    },
                    {
                        "key": "YW1vdW50",
                        "value": "MTAwMHVhdG9t",
                        "index": true
                    }
                ]
            },
            {
                "type": "message",
                "attributes": [
                    {
                        "key": "c2VuZGVy",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    }
                ]
            },
            {
                "type": "tx",
                "attributes": [
                    {
                        "key": "ZmVl",
                        "value": "MTAwMHVhdG9t",
                        "index": true
                    },
                    {
                        "key": "ZmVlX3BheWVy",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    }
                ]
            },
            {
                "type": "tx",
                "attributes": [
                    {
                        "key": "YWNjX3NlcQ==",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFzLzQ=",
                        "index": true
                    }
                ]
            },
            {
                "type": "tx",
                "attributes": [
                    {
                        "key": "c2lnbmF0dXJl",
                        "value": "WUlwSmREZ2hEQ050L3VCUWk1UUhHOEFRRU1qbmpkWFJ5cEp2VmtDRWdQVXprSnpUR3RHQ041RzE4dWJWV2YwUFh6UzBicm1CSGZTNHBoY200a0dZVXc9PQ==",
                        "index": true
                    }
                ]
            },
            {
                "type": "message",
                "attributes": [
                    {
                        "key": "YWN0aW9u",
                        "value": "L2Nvc21vcy5iYW5rLnYxYmV0YTEuTXNnU2VuZA==",
                        "index": true
                    }
                ]
            },
            {
                "type": "coin_spent",
                "attributes": [
                    {
                        "key": "c3BlbmRlcg==",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    },
                    {
                        "key": "YW1vdW50",
                        "value": "MTQ4MDAwMHVhdG9t",
                        "index": true
                    }
                ]
            },
            {
                "type": "coin_received",
                "attributes": [
                    {
                        "key": "cmVjZWl2ZXI=",
                        "value": "Y29zbW9zMXBzcjV4M2tncmE1ZnZtNGdjNGw2dWZ5a24wbmwzZXNkamVleDhu",
                        "index": true
                    },
                    {
                        "key": "YW1vdW50",
                        "value": "MTQ4MDAwMHVhdG9t",
                        "index": true
                    }
                ]
            },
            {
                "type": "transfer",
                "attributes": [
                    {
                        "key": "cmVjaXBpZW50",
                        "value": "Y29zbW9zMXBzcjV4M2tncmE1ZnZtNGdjNGw2dWZ5a24wbmwzZXNkamVleDhu",
                        "index": true
                    },
                    {
                        "key": "c2VuZGVy",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    },
                    {
                        "key": "YW1vdW50",
                        "value": "MTQ4MDAwMHVhdG9t",
                        "index": true
                    }
                ]
            },
            {
                "type": "message",
                "attributes": [
                    {
                        "key": "c2VuZGVy",
                        "value": "Y29zbW9zMWEwZDIwNm5ueWxweGY4dGE5a2NyZmY1bXVjamE3aDIyOHh3eHFz",
                        "index": true
                    }
                ]
            },
            {
                "type": "message",
                "attributes": [
                    {
                        "key": "bW9kdWxl",
                        "value": "YmFuaw==",
                        "index": true
                    }
                ]
            }
        ]
    }
}
```
{% endcode %}
