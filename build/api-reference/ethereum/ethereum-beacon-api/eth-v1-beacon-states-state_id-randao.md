---
description: >-
  Fetch the RANDAO mix for the requested epoch from the state identified by
  state_id.
---

# /eth/v1/beacon/states/{state\_id}/randao

If an epoch is not specified then the RANDAO mix for the state's current epoch will be returned.

By adjusting the `state_id` parameter you can query for any historic value of the RANDAO mix. Ordinarily states from the same epoch will mutate the RANDAO mix for that epoch as blocks are applied.

#### P**arameters:**

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/states/head/randao


// Result
{
    "execution_optimistic": false,
    "finalized": false,
    "data": {
        "randao": "0x32783c1d38686a29ff9c492caae0216805b73815130391aa218b3e20e31d65ae"
    }
}
```
{% endcode %}
