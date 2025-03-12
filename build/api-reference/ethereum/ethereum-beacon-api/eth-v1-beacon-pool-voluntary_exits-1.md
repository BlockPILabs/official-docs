---
description: >-
  Submits SignedVoluntaryExit object to node's pool and if passes validation
  node MUST broadcast it to network.
---

# /eth/v1/beacon/pool/voluntary\_exits

#### Parameters:

None

**Request body:**

The SignedVoluntaryExit objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/voluntary_exits
‘
<SignedVoluntaryExit object>
’

// Result

```
{% endcode %}
