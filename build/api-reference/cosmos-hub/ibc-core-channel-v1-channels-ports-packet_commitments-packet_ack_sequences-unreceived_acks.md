---
description: >-
  UnreceivedAcks returns all the unreceived IBC acknowledgements associated with
  a channel and sequences.
---

# /ibc/core/channel/v1/channels/{}/ports/{}/packet\_commitments/{packet\_ack\_sequences}/unreceived\_acks

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

**packet\_ack\_sequences - string**, packet sequence

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost/packet_commitments/1/unreceived_acks

// Result
{
    "sequences": [],
    "height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
