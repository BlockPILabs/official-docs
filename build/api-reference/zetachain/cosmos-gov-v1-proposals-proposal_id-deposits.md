---
description: Deposits queries all deposits of a single proposal.
---

# /cosmos/gov/v1/proposals/{proposal\_id}/deposits

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/proposals/1/deposits

// Result
{
  "deposits": [
  ],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
```
{% endcode %}
