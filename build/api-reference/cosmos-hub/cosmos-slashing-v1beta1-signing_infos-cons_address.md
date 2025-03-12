---
description: SigningInfo queries the signing info of given cons address
---

# /cosmos/slashing/v1beta1/signing\_infos/{cons\_address}

#### **Parameters:**

**cons\_address - string**, cons\_address is the address to query signing info of

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/slashing/v1beta1/signing_infos/cosmosvalcons1gvz5lwpu389ajz0s5ssqm59508mk2lscav4emm

// Result
{
    "val_signing_info": {
        "address": "cosmosvalcons1gvz5lwpu389ajz0s5ssqm59508mk2lscav4emm",
        "start_height": "10563361",
        "index_offset": "56907",
        "jailed_until": "1970-01-01T00:00:00Z",
        "tombstoned": false,
        "missed_blocks_counter": "0"
    }
}
```
{% endcode %}
