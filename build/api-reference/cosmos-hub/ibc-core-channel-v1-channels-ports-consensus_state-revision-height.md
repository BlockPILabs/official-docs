---
description: >-
  ChannelConsensusState queries for the consensus state for the channel
  associated with the provided channel identifiers.
---

# /ibc/core/channel/v1/channels/{}/ports/{}/consensus\_state/revision/{}/height/{}

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

**revision\_number- string**, revision number of the consensus state

**revision\_height- string**, revision height of the consensus state

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/channel/v1/channels/channel-370/ports/icahost/consensus_state/revision/1/height/0x2990e2

// Result
{
    "consensus_state": {
        "@type": "/ibc.lightclients.tendermint.v1.ConsensusState",
        "timestamp": "2023-02-15T23:18:06.986816910Z",
        "root": {
            "hash": "fdV2/Hf6wf+Jd/tIg6vsHs8rrp6WNLX0+vC7449Gf6M="
        },
        "next_validators_hash": "632DCF961AB03EC9D0092F006F5869EB053D692ABBDEAE2521968460C1AF53AB"
    },
    "client_id": "07-tendermint-892",
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
