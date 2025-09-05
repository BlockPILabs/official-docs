---
description: PacketCommitment queries a stored packet commitment hash.
---

# /ibc/core/channel/v1/channels/{}/ports/{}/packet\_commitments/{sequence}

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

**sequence** **- string**, packet sequence

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/channel/v1/channels/channel-0/ports/transfer/packet_commitments/1

// Result
{
    "commitment": "P48OX2zrDqI5qt/BCRk5oLAajUTGOhBkEzRB5+IL8bc=",
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
