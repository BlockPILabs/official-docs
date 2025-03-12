---
description: >-
  ConsensusState queries a consensus state associated with a client state at a
  given height.
---

# /ibc/core/client/v1/consensus\_states/{client\_id}/revision/{}/height/{}

#### **Parameters:**

**client\_id - string**, client identifier

**revision\_number - string**, revision number of the consensus state

**revision\_height - string**, revision height of the consensus state

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/client/v1/consensus_states/07-tendermint-1001/revision/1/height/2030274

// Result
{
    "consensus_state": {
        "@type": "/ibc.lightclients.tendermint.v1.ConsensusState",
        "timestamp": "2022-12-02T19:46:25.199178279Z",
        "root": {
            "hash": "mOweP7CU9FDCn48OAcZGk+hncnYaqZF9Ct9CMa+ftfc="
        },
        "next_validators_hash": "5039BFECD47F8FF71E7C34A5A8579379084E6BC13539369E123C2353C9201B7C"
    },
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
