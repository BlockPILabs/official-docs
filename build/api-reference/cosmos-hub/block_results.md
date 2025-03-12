---
description: >-
  Get block_results. When the discard_abci_responses storage flag is enabled,
  this endpoint will return an error.
---

# /block\_results

If the `height` field is set to a non-default value, upon success, the `Cache-Control` header will be set with the default maximum age.

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch information regarding the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/block_results

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "height": "14183822",
        "txs_results": [
            {
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
                    ......
                 ]
             }
        ],
        "end_block_events": null,
        "validator_updates": [
            {
                "pub_key": {
                    "Sum": {
                        "type": "tendermint.crypto.PublicKey_Ed25519",
                        "value": {
                            "ed25519": "5qKdBzdr8XHw2BWR/8yEceFRWEjGpzsqBo6q0OVkf9g="
                        }
                    }
                },
                "power": "2602853"
            }
        ],
        "consensus_param_updates": {
            "block": {
                "max_bytes": "200000",
                "max_gas": "40000000"
            },
            "evidence": {
                "max_age_num_blocks": "1000000",
                "max_age_duration": "172800000000000",
                "max_bytes": "50000"
            },
            "validator": {
                "pub_key_types": [
                    "ed25519"
                ]
            }
        }
    }
}
```
{% endcode %}
