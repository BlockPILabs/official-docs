---
description: >-
  Retrieves BLS to execution changes known by the node but not necessarily
  incorporated into any block
---

# /eth/v1/beacon/pool/bls\_to\_execution\_changes

#### Parameters:

None



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/bls_to_execution_changes

// Result
{
    "data": []
}
```
{% endcode %}
