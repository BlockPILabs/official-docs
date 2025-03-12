---
description: >-
  Get a transaction.  Upon success, the Cache-Control header will be set with
  the default maximum age.
---

# /tx

#### **Parameters:**

**hash- string**, hash of transaction to retrieve

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/tx?hash=0x547DC59DD6EE54082183A5F75F1D350BE4D271825BB75C6A626F74DAE2FA2489

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "hash": "547DC59DD6EE54082183A5F75F1D350BE4D271825BB75C6A626F74DAE2FA2489",
        "height": "14183822",
        "index": 0,
        "tx_result": {
            "code": 0,
            "data": "Ch4KHC9jb3Ntb3MuYmFuay52MWJldGExLk1zZ1NlbmQ=",
            "log": "[{\"events\":[{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"cosmos1f0d77kqccjcz95r4py478zppgwl3pl8w4x9s0p\"},{\"key\":\"amount\",\"value\":\"1719939uatom\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"cosmos1s5z672rlcfy596xvm3q2c4phfhg9pk704654af\"},{\"key\":\"amount\",\"value\":\"1719939uatom\"}]},{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"/cosmos.bank.v1beta1.MsgSend\"},{\"key\":\"sender\",\"value\":\"cosmos1s5z672rlcfy596xvm3q2c4phfhg9pk704654af\"},{\"key\":\"module\",\"value\":\"bank\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"cosmos1f0d77kqccjcz95r4py478zppgwl3pl8w4x9s0p\"},{\"key\":\"sender\",\"value\":\"cosmos1s5z672rlcfy596xvm3q2c4phfhg9pk704654af\"},{\"key\":\"amount\",\"value\":\"1719939uatom\"}]}]}]",
            "info": "",
            "gas_wanted": "91770",
            "gas_used": "69111",
            "events": [
                {
                    "type": "coin_spent",
                    "attributes": [
                        {
                            "key": "c3BlbmRlcg==",
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "MjI5NXVhdG9t",
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
                            "value": "MjI5NXVhdG9t",
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
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "MjI5NXVhdG9t",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "c2VuZGVy",
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx",
                    "attributes": [
                        {
                            "key": "ZmVl",
                            "value": "MjI5NXVhdG9t",
                            "index": true
                        },
                        {
                            "key": "ZmVlX3BheWVy",
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx",
                    "attributes": [
                        {
                            "key": "YWNjX3NlcQ==",
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFmLzI3Ng==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx",
                    "attributes": [
                        {
                            "key": "c2lnbmF0dXJl",
                            "value": "ZGU4amlyQ2FxVTVzUHZsMHdQcXhrdDFWL3hvbkUzYldzWEY2bm5YVWdwWjRIbmVyTzkrRmhUL2NVbmZGSDBiUWZNbjRnQnVvek1xdlFtWGNSS2JBTkE9PQ==",
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
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "MTcxOTkzOXVhdG9t",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "coin_received",
                    "attributes": [
                        {
                            "key": "cmVjZWl2ZXI=",
                            "value": "Y29zbW9zMWYwZDc3a3FjY2pjejk1cjRweTQ3OHpwcGd3bDNwbDh3NHg5czBw",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "MTcxOTkzOXVhdG9t",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "transfer",
                    "attributes": [
                        {
                            "key": "cmVjaXBpZW50",
                            "value": "Y29zbW9zMWYwZDc3a3FjY2pjejk1cjRweTQ3OHpwcGd3bDNwbDh3NHg5czBw",
                            "index": true
                        },
                        {
                            "key": "c2VuZGVy",
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "MTcxOTkzOXVhdG9t",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "c2VuZGVy",
                            "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
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
            ],
            "codespace": ""
        },
        "tx": "CpMBCpABChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEnAKLWNvc21vczFzNXo2NzJybGNmeTU5Nnh2bTNxMmM0cGhmaGc5cGs3MDQ2NTRhZhItY29zbW9zMWYwZDc3a3FjY2pjejk1cjRweTQ3OHpwcGd3bDNwbDh3NHg5czBwGhAKBXVhdG9tEgcxNzE5OTM5EmgKUQpGCh8vY29zbW9zLmNyeXB0by5zZWNwMjU2azEuUHViS2V5EiMKIQNFCHM2H9opAAax5ybDYM5LYJY+0Qod3RJxZD5n+3g7cxIECgIIfxiUAhITCg0KBXVhdG9tEgQyMjk1EPrMBRpAde8jirCaqU5sPvl0wPqxkt1V/xonE3bWsXF6nnXUgpZ4HnerO9+FhT/cUnfFH0bQfMn4gBuozMqvQmXcRKbANA=="
    }
}                  
```
{% endcode %}
