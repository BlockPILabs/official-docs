---
description: SigningInfos queries signing info of all validators
---

# /cosmos/slashing/v1beta1/signing\_infos

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/slashing/v1beta1/signing_infos

// Result
{
    "info": [
        {
            "address": "",
            "start_height": "0",
            "index_offset": "17190430",
            "jailed_until": "1970-01-01T00:00:00Z",
            "tombstoned": false,
            "missed_blocks_counter": "0"
        },
        {
            "address": "cosmosvalcons1gvz5lwpu389ajz0s5ssqm59508mk2lscav4emm",
            "start_height": "10563361",
            "index_offset": "56907",
            "jailed_until": "1970-01-01T00:00:00Z",
            "tombstoned": false,
            "missed_blocks_counter": "0"
        }
    ],
    "pagination": {
        "next_key": "FEPIXqaRYzd9UgyKNh/j0VKBipcK",
        "total": "411"
    }
}
```
{% endcode %}
