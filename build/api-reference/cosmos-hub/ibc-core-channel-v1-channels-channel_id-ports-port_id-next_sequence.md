---
description: NextSequenceReceive returns the next receive sequence for a given channel.
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}/next\_sequence

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/channel/v1/channels/channel-370/ports/icahost/next_sequence

// Result
{
    "next_sequence_receive": "175",
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
