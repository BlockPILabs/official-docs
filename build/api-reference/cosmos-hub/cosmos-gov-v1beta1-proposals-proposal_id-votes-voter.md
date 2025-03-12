---
description: Vote queries voted information based on proposalID, voterAddr.
---

# /cosmos/gov/v1beta1/proposals/{proposal\_id}/votes/{voter}

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

**voter - string**, voter defines the oter address for the proposals.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1beta1/proposals/98/votes/cosmos1q8xkawx85p04y5xt6ejd89nl5deurshwwzucqy

// Result
{
    "vote": {
        "proposal_id": "98",
        "voter": "cosmos1q8xkawx85p04y5xt6ejd89nl5deurshwwzucqy",
        "option": "VOTE_OPTION_YES",
        "options": [
            {
                "option": "VOTE_OPTION_YES",
                "weight": "1.000000000000000000"
            }
        ]
    }
}
```
{% endcode %}
