---
description: >-
  Submits a list of SignedBLSToExecutionChange objects to node's pool. Any that
  pass validation MUST be broadcast to the network.
---

# /eth/v1/beacon/pool/bls\_to\_execution\_changes

#### Parameters:

None

**Request body:**

The SignedBLSToExecutionChange objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/bls_to_execution_changes
‘
<SignedBLSToExecutionChange object>
’

// Result

```
{% endcode %}
