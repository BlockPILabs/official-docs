---
description: TallyResult queries the tally of a proposal vote.
---

# /cosmos/gov/v1beta1/proposals/{proposal\_id}/tally

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1beta1/proposals/99/tally
// Result
{
    "tally": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
    }
}
```
{% endcode %}
