---
description: >-
  Get the withdrawals computed from the specified state, that will be included
  in the block that gets built on the specified state.
---

# /eth/v1/builder/states/{state\_id}/expected\_withdrawals

#### Parameters:

**state\_id-string**, State identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", "justified", , \<hex encoded stateRoot with 0x prefix>.



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/builder/states/{state_id}/expected_withdrawals


// Result
{
    "execution_optimistic": false,
    "finalized": false,
    "data": [
        {
            "index": "45629483",
            "validator_index": "695576",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18365795"
        },
        {
            "index": "45629484",
            "validator_index": "695577",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18329885"
        },
        {
            "index": "45629485",
            "validator_index": "695578",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18228179"
        },
        {
            "index": "45629486",
            "validator_index": "695579",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18360235"
        },
        {
            "index": "45629487",
            "validator_index": "695580",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18403925"
        },
        {
            "index": "45629488",
            "validator_index": "695581",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18339686"
        },
        {
            "index": "45629489",
            "validator_index": "695582",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18411930"
        },
        {
            "index": "45629490",
            "validator_index": "695583",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18392993"
        },
        {
            "index": "45629491",
            "validator_index": "695584",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18360493"
        },
        {
            "index": "45629492",
            "validator_index": "695585",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18412376"
        },
        {
            "index": "45629493",
            "validator_index": "695586",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18330143"
        },
        {
            "index": "45629494",
            "validator_index": "695587",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18332267"
        },
        {
            "index": "45629495",
            "validator_index": "695588",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18359293"
        },
        {
            "index": "45629496",
            "validator_index": "695589",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18308407"
        },
        {
            "index": "45629497",
            "validator_index": "695590",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18401238"
        },
        {
            "index": "45629498",
            "validator_index": "695591",
            "address": "0x45aa934d0c1cf5ad7af723fff4639819fdf6a123",
            "amount": "18459335"
        }
    ]
}
```
{% endcode %}
