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
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/consensus_state

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "round_state": {
            "height/round/step": "14184146/0/6",
            "start_time": "2023-02-22T07:37:00.616241179Z",
            "proposal_block_hash": "53842DAB6E50A7CCD31DA050B7F24AA541BD14275131D0E5058CF4BE197F8FB8",
            "locked_block_hash": "53842DAB6E50A7CCD31DA050B7F24AA541BD14275131D0E5058CF4BE197F8FB8",
            "valid_block_hash": "53842DAB6E50A7CCD31DA050B7F24AA541BD14275131D0E5058CF4BE197F8FB8",
            "height_vote_set": [
                {
                    "round": 0,
                    "prevotes": [
                        "Vote{0:AC2D56057CD8 14184146/00/SIGNED_MSG_TYPE_PREVOTE(Prevote) 53842DAB6E50 9990B633529B @ 2023-02-22T07:37:00.888869091Z}",
                        ......
                    ],
                    "precommits_bit_array": "BA{175:_______________________________________________________________________________________________________________________________________________________________________________} 0/209388120 = 0.00"
                }
            ],
            "proposer": {
                "address": "846BE4F39E3122D2A2D3FE5454E2561073E95538",
                "index": 34
            }
        }
    }
}
```
{% endcode %}
