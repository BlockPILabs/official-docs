---
description: >-
  Retrieve attestation reward info for validators specified by array of public
  keys or validator index. If no array is provided, return reward info for every
  validator.
---

# /eth/v1/beacon/blinded\_blocks/{block\_id}

#### P**arameters:**

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/blinded_blocks/head


// Result

```
{% endcode %}
