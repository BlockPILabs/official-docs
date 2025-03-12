---
description: >-
  ConsensusStates queries all the consensus state associated with a given
  client.
---

# /ibc/core/client/v1/consensus\_states/{client\_id}

#### **Parameters:**

**client\_id - string**, client unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/client/v1/consensus_states/07-tendermint-0

// Result
{
    "consensus_states": [],
    "pagination": {
        "next_key": null,
        "total": "0"
    }
}
```
{% endcode %}
