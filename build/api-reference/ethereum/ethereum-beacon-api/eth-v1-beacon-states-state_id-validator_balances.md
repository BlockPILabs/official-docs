---
description: Returns filterable list of validators balances.
---

# /eth/v1/beacon/states/{state\_id}/validator\_balances

Balances will be returned for all indices or public key that match known validators. If an index or public key does not match any known validator, no balance will be returned but this will not cause an error. There are no guarantees for the returned data in terms of ordering; the index is returned for each balance, and can be used to confirm for which inputs a response has been returned.

#### P**arameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/head/validator_balances

// Result
as described above
```
{% endcode %}
