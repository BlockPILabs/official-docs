---
description: >-
  Retrieves proposer slashings known by the node but not necessarily
  incorporated into any block
---

# /eth/v1/beacon/pool/proposer\_slashings

#### Parameters:

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/proposer_slashings

// Result
{
  "data": []
}
```
{% endcode %}
