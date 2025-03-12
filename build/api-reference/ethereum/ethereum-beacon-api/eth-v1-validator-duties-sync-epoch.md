---
description: >-
  Requests the beacon node to provide a set of sync committee duties for a
  particular epoch.
---

# /eth/v1/validator/duties/sync/{epoch}



#### Parameters:

**epoch-string,** epoch // EPOCHS\_PER\_SYNC\_COMMITTEE\_PERIOD <= current\_epoch // EPOCHS\_PER\_SYNC\_COMMITTEE\_PERIOD + 1



**Request body:**

An array of the validator indices for which to obtain the duties.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST-H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/duties/sync/284100
‘
[
  "1"
]
’
// Result
{
    "execution_optimistic": false,
    "data": []
}
```
{% endcode %}
