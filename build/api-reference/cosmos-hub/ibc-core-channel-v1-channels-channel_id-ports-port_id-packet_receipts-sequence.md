---
description: >-
  PacketReceipt queries if a given packet sequence has been received on the
  queried chain
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}/packet\_receipts/{sequence}

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

**sequence** **- string**, packet sequence

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost/packet_receipts/1

// Result
{
    "received": false,
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}

