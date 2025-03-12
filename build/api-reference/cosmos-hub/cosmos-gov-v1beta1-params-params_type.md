---
description: Params queries all parameters of the gov module.
---

# /cosmos/gov/v1beta1/params/{params\_type}

#### **Parameters:**

**params\_type - string**, params\_type defines which parameters to query for, can be one of "voting",\
"tallying" or "deposit".

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1beta1/params/voting

// Result
{
    "voting_params": {
        "voting_period": "1209600s"
    },
    "deposit_params": {
        "min_deposit": [],
        "max_deposit_period": "0s"
    },
    "tally_params": {
        "quorum": "0.000000000000000000",
        "threshold": "0.000000000000000000",
        "veto_threshold": "0.000000000000000000"
    }
}
```
{% endcode %}
