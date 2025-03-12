---
description: Votes queries votes of a given proposal.
---

# /cosmos/gov/v1beta1/proposals/{proposal\_id}/votes

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1beta1/proposals/98/votes

// Result
{
    "votes": [
        {
            "proposal_id": "98",
            "voter": "cosmos1qqqzhvucv6375szzc5mh7n0290fd4j38pv6yaj",
            "option": "VOTE_OPTION_NO",
            "options": [
                {
                    "option": "VOTE_OPTION_NO",
                    "weight": "1.000000000000000000"
                }
            ]
        },
        ......
    ],
    "pagination": {
        "next_key": "FAHR/8akPH1SOx4PE37I9+tDA870",
        "total": "13859"
    }
}
```
{% endcode %}
