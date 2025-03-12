---
description: >-
  Get consensus state.  Not safe to call from inside the ABCI application during
  a block execution.
---

# /dump\_consensus\_state

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/dump_consensus_state

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "round_state": {
            "height": "2115738",
            "round": 0,
            "step": 4,
            "start_time": "2023-03-31T06:50:00.152750061Z",
            "commit_time": "2023-03-31T06:49:55.152750061Z",
            "validators": {
                "validators": [
                    {
                        "address": "0CE77A66422692185F4EE7DAFC212D2A2294BBAE",
                        "pub_key": {
                            "type": "tendermint/PubKeyEd25519",
                            "value": "IYYt/r5YgdxYhwPWivBOgfGGBXMtd2ChQ8qv5RWqhvI="
                        },
                        "voting_power": "5000001000000",
                        "proposer_priority": "-1625238253889"
                    },
                    ......
                ],
                "proposer": {
                    "address": "0CE77A66422692185F4EE7DAFC212D2A2294BBAE",
                    "pub_key": {
                        "type": "tendermint/PubKeyEd25519",
                        "value": "IYYt/r5YgdxYhwPWivBOgfGGBXMtd2ChQ8qv5RWqhvI="
                    },
                    "voting_power": "5000001000000",
                    "proposer_priority": "-6625239253889"
                }
            },
            "triggered_timeout_precommit": false
        },
        "peers": [
            {
                "node_address": "d046a7d785accd74bb0d7b4405749ed6b3280e92@152.32.150.236:26656",
                "peer_state": {
                    "round_state": {
                        "height": "2115738",
                        "round": 0,
                        "step": 3,
                        "start_time": "2023-03-31T06:50:00.160142932Z",
                        "proposal": true,
                        "proposal_block_part_set_header": {
                            "total": 1,
                            "hash": "071D7E8D7E4163186ACA324144445A4078D3197FC81A6398EEA0D25121A8BFCE"
                        },
                        "proposal_block_parts": "x",
                        "proposal_pol_round": -1,
                        "proposal_pol": null,
                        "prevotes": "___x__",
                        "precommits": "______",
                        "last_commit_round": 0,
                        "last_commit": "xxxxxx",
                        "catchup_commit_round": -1,
                        "catchup_commit": "______"
                    },
                    "stats": {
                        "votes": "63219",
                        "block_parts": "1563"
                    }
                }
            },
            ......
        ]
    }
}    
```
{% endcode %}
