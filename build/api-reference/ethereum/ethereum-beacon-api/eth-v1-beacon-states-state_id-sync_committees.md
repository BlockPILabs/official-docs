---
description: >-
  Retrieves the current sync committee for the given state. Also returns the
  subcommittee assignments.
---

# /eth/v1/beacon/states/{state\_id}/sync\_committees

#### P**arameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/head/sync_committees


// Result
as described above
```
{% endcode %}
