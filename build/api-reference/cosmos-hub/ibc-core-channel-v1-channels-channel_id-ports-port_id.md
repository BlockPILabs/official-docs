---
description: Channel queries an IBC Channel.
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost

// Result
{
    "channel": {
        "state": "STATE_OPEN",
        "ordering": "ORDER_ORDERED",
        "counterparty": {
            "port_id": "icacontroller-uratom-0-withdrawal",
            "channel_id": "channel-2"
        },
        "connection_hops": [
            "connection-618"
        ],
        "version": "{\"version\":\"ics27-1\",\"controller_connection_id\":\"connection-0\",\"host_connection_id\":\"connection-618\",\"address\":\"cosmos1tne2mwtwgeeh2hr4vw9vt0uj5s4dln5qga7f7llmmqrydewwafds6zmjq4\",\"encoding\":\"proto3\",\"tx_type\":\"sdk_multi_msg\"}"
    },
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
