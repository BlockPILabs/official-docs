---
description: Votes queries votes of a given proposal.
---

# /cosmos/gov/v1/proposals/{proposal\_id}/votes

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/proposals/1/votes

// Result
{
    "votes": [  ],
    "pagination": {
        "next_key": null,
        "total": "0"
    }
}
```
{% endcode %}
