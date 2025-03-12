---
description: >-
  Submits AttesterSlashing object to node's pool and if passes validation node
  MUST broadcast it to network.
---

# /eth/v1/beacon/pool/proposer\_slashings

#### Parameters:

None

**Request body:**

The ProposerSlashing object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/proposer_slashings
‘
<ProposerSlashing object>
’

// Result

```
{% endcode %}
