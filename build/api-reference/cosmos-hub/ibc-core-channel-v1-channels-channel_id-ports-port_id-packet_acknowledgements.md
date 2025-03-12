---
description: >-
  PacketAcknowledgements returns all the packet acknowledgements associated with
  a channel.
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}/packet\_acknowledgements

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost/packet_acknowledgements

// Result
{
    "acknowledgements": [
        {
            "port_id": "icahost",
            "channel_id": "channel-370",
            "sequence": "1",
            "data": "GJEiwELm3evrerbpTVUsggc64Pw9TEyrPYesGmUxNM8="
        },
        ......
    ],
    "pagination": {
        "next_key": "LzMy",
        "total": "174"
    },
    "height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
