---
description: >-
  Returns validator specified by state and id or public key along with status
  and balance.
---

# /eth/v1/beacon/states/{state\_id}/validators/{validator\_id}

#### P**arameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.\
\
**validator\_id-string**, Either hex encoded public key (any bytes48 with 0x prefix) or validator index

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/finalized/validators/0x8e323fd501233cd4d1b9d63d74076a38de50f2f584b001a5ac2412e4e46adb26d2fb2a6041e7e8c57cd4df0916729219

// Result
as described above
```
{% endcode %}
