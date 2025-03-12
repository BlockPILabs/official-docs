---
description: PacketAcknowledgement queries a stored packet acknowledgement hash.
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}/packet\_acks/{sequence}

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

**sequence** **- string**, packet sequence

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost/packet_acks/1

// Result
{
    "acknowledgement": "GJEiwELm3evrerbpTVUsggc64Pw9TEyrPYesGmUxNM8=",
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
