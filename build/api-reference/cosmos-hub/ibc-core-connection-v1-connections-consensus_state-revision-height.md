---
description: >-
  ConnectionConsensusState queries the consensus state associated with the
  connection.
---

# /ibc/core/connection/v1/connections/{}/consensus\_state/revision/{}/height/{}

#### **Parameters:**

**connection\_id - string**, connection unique identifier

**revision\_number- string**, consensus state revision number

**revision\_height - string**, consensus state revision height

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/connection/v1/connections/connection-187/consensus_state/revision/1/height/17409098

// Result
{
    "consensus_state": {
        "@type": "/ibc.lightclients.tendermint.v1.ConsensusState",
        "timestamp": "2022-11-14T20:40:16.699477529Z",
        "root": {
            "hash": "DT+9BJKgpeubRgPrGMffdEtliqqkLAjYtQxE+0A1wXI="
        },
        "next_validators_hash": "794FAB6CAFA942508FEBC313177B080FF13211CEC1EA71D90833F98AC6AA8000"
    },
    "client_id": "07-tendermint-141",
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
