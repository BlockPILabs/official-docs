---
description: >-
  Retrieves rewards info for sync committee members specified by array of public
  keys or validator index. If no array is provided, return reward info for every
  committee member.
---

# /eth/v1/beacon/rewards/sync\_committee/{block\_id}

#### Parameters:

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.

**Request body:**

An array of either hex encoded public key (any bytes48 with 0x prefix) or validator index

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/rewards/sync_committee/head

'
[
  "722032"
]
'

// Result

```
{% endcode %}
