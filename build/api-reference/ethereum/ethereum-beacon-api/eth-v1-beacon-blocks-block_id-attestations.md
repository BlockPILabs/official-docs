---
description: Retrieves attestation included in requested block.
---

# /eth/v1/beacon/blocks/{block\_id}/attestations

#### P**arameters:**

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/blocks/head/attestations


// Result

```
{% endcode %}
