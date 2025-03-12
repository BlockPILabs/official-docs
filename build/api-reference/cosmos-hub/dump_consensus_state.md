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
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/dump_consensus_state

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "round_state": {
            "height": "14184114",
            "round": 0,
            "step": 1,
            "start_time": "2023-02-22T07:33:39.262530271Z",
            "commit_time": "2023-02-22T07:33:34.262530271Z",
            "validators": {
                "validators": [
                    {
                        "address": "AC2D56057CD84765E6FBE318979093E8E44AA18F",
                        "pub_key": {
                            "type": "tendermint/PubKeyEd25519",
                            "value": "0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI="
                        },
                        "voting_power": "12376400",
                        "proposer_priority": "-87008689"
                    },
                    ......
                ],
                "proposer": {
                    "address": "AC2D56057CD84765E6FBE318979093E8E44AA18F",
                    "pub_key": {
                        "type": "tendermint/PubKeyEd25519",
                        "value": "0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI="
                    },
                    "voting_power": "12376400",
                    "proposer_priority": "-99385089"
                }
            },
            "triggered_timeout_precommit": false
        },
        "peers": [
            {
                "node_address": "72829b78b38408b03793ed389b9f16596b82c306@146.59.81.92:26656",
                "peer_state": {
                    "round_state": {
                        "height": "14184114",
                        "round": 0,
                        "step": 1,
                        "start_time": "2023-02-22T07:33:39.304523702Z",
                        "proposal": false,
                        "proposal_block_part_set_header": {
                            "total": 0,
                            "hash": ""
                        },
                        "proposal_block_parts": null,
                        "proposal_pol_round": -1,
                        "proposal_pol": "_______________________________________________________________________________________________________________________________________________________________________________",
                        "prevotes": "_______________________________________________________________________________________________________________________________________________________________________________",
                        "precommits": "_______________________________________________________________________________________________________________________________________________________________________________",
                        "last_commit_round": 0,
                        "last_commit": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxxxxxx",
                        "catchup_commit_round": -1,
                        "catchup_commit": "_______________________________________________________________________________________________________________________________________________________________________________"
                    },
                    "stats": {
                        "votes": "2723913",
                        "block_parts": "4327"
                    }
                }
            }
        ]
    }
}
```
{% endcode %}
