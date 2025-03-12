---
description: >-
  Get consensus state.  Not safe to call from inside the ABCI application during
  a block execution.
---

# /consensus\_state

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/consensus_state

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "round_state": {
            "height/round/step": "2116324/0/1",
            "start_time": "2023-03-31T07:41:54.178649564Z",
            "proposal_block_hash": "",
            "locked_block_hash": "",
            "valid_block_hash": "",
            "height_vote_set": [
                {
                    "round": 0,
                    "prevotes": [
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote"
                    ],
                    "prevotes_bit_array": "BA{6:______} 0/20000005100005 = 0.00",
                    "precommits": [
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote",
                        "nil-Vote"
                    ],
                    "precommits_bit_array": "BA{6:______} 0/20000005100005 = 0.00"
                }
            ],
            "proposer": {
                "address": "8D5804BDEFA39EDFA488062C1F67718250C366CD",
                "index": 2
            }
        }
    }
}
```
{% endcode %}
