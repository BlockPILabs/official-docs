---
description: >-
  Requests that the beacon node identify information about its implementation in
  a format similar to a HTTP User-Agent field.
---

# /eth/v1/node/version



#### Parameters:

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/node/version

// Result
{
    "data": {
        "version": "Lighthouse/v5.1.3-3058b96/x86_64-linux"
    }
}
```
{% endcode %}
