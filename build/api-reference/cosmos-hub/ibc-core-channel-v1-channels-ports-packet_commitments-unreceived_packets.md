---
description: >-
  UnreceivedPackets returns all the unreceived IBC packets associated with a
  channel and sequences.
---

# /ibc/core/channel/v1/channels/{}/ports/{}/packet\_commitments/{}/unreceived\_packets

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

**packet\_commitment\_sequences - string**, list of packet sequences

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost/packet_commitments/1/unreceived_packets

// Result
{
    "sequences": [
        "1"
    ],
    "height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
