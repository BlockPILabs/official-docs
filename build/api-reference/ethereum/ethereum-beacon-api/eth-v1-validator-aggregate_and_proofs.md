---
description: >-
  Verifies given aggregate and proofs and publishes them on appropriate
  gossipsub topic.
---

# /eth/v1/validator/aggregate\_and\_proofs

#### Parameters:

**None**

**Request body:**

aggregate and proofs

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/aggregate_and_proofs
'
<aggregate and proofs>
'

// Result

```
{% endcode %}
