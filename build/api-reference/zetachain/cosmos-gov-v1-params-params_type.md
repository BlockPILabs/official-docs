---
description: Params queries all parameters of the gov module.
---

# /cosmos/gov/v1/params/{params\_type}

#### **Parameters:**

**params\_type-string**, params\_type defines which parameters to query for, can be one of "voting", "tallying" or "deposit".

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/params/voting

// Result
{
  "voting_params": {
    "voting_period": "43200s"
  },
  "deposit_params": null,
  "tally_params": null
}
```
{% endcode %}
