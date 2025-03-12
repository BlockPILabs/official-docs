---
description: >-
  Retrieves block details for given block id. Depending on Accept header it can
  be returned either as json or as bytes serialized by SSZ
---

# /eth/v2/beacon/blocks/{block\_id}

#### P**arameters:**

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v2/beacon/blocks/head


// Result

```
{% endcode %}
