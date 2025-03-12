---
description: Retrieve Eth1 deposit contract address and chain ID.
---

# /eth/v1/config/deposit\_contract



#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/config/deposit_contract

// Result
{
    "data": {
        "chain_id": "1",
        "address": "0x00000000219ab540356cbb839cbe05303d7705fa"
    }
}
```
{% endcode %}
