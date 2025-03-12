---
description: Returns filterable list of validators with their balance, status and index.
---

# /eth/v1/beacon/states/{state\_id}/validators

Information will be returned for all indices or public key that match known validators. If an index or public key does not match any known validator, no information will be returned but this will not cause an error. There are no guarantees for the returned data in terms of ordering; both the index and public key are returned for each validator, and can be used to confirm for which inputs a response has been returned.

#### **Parameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/finalized/validators

// Result
as described above
```
{% endcode %}
