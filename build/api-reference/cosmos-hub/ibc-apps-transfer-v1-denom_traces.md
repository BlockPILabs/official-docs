---
description: DenomTraces queries all denomination traces.
---

# /ibc/apps/transfer/v1/denom\_traces

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/apps/transfer/v1/denom_traces

// Result
{
    "denom_traces": [
        {
            "path": "transfer/channel-109",
            "base_denom": "basecro"
        },
        {
            "path": "transfer/channel-126",
            "base_denom": "stake"
        },
        {
            "path": "transfer/channel-129",
            "base_denom": "token"
        },
        {
            "path": "transfer/channel-140",
            "base_denom": "moon"
        },
        {
            "path": "transfer/channel-141/transfer/channel-1/transfer/channel-17/transfer/channel-141/transfer/channel-1/transfer/channel-17/transfer/channel-141/transfer/channel-1/transfer/channel-17/transfer/channel-141/transfer/channel-1",
            "base_denom": "uakt"
        },
        ...
     ],
    "pagination": {
        "next_key": "I50KVBfrcPS1GagpkpAP3Y1RiFkFyJPJGUVA3XkmHq4=",
        "total": "634"
    }
}       
```
{% endcode %}
