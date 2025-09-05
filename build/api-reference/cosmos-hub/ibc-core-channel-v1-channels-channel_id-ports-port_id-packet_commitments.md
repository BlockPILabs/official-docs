---
description: >-
  PacketCommitments returns all the packet commitments hashes associated with a
  channel.
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}/packet\_commitments

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/channel/v1/channels/channel-370/ports/icahost/packet_commitments

// Result
{
    "commitments": [],
    "pagination": {
        "next_key": null,
        "total": "0"
    },
    "height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
