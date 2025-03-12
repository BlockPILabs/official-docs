---
description: Retrieve all forks, past present and future, of which this node is aware.
---

# /eth/v1/config/fork\_schedule

#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/config/fork_schedule


// Result
{
    "data": [
        {
            "previous_version": "0x00000000",
            "current_version": "0x00000000",
            "epoch": "0"
        },
        {
            "previous_version": "0x00000000",
            "current_version": "0x01000000",
            "epoch": "74240"
        },
        {
            "previous_version": "0x01000000",
            "current_version": "0x02000000",
            "epoch": "144896"
        },
        {
            "previous_version": "0x02000000",
            "current_version": "0x03000000",
            "epoch": "194048"
        },
        {
            "previous_version": "0x03000000",
            "current_version": "0x04000000",
            "epoch": "269568"
        }
    ]
}
```
{% endcode %}
