---
description: ConnectionChannels queries all the channels associated with a connection end.
---

# /ibc/core/channel/v1/connections/{connection}/channels

#### **Parameters:**

**connection- string**, connection unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/connections/connection-618/channels

// Result
{
    "channels": [
        {
            "state": "STATE_OPEN",
            "ordering": "ORDER_ORDERED",
            "counterparty": {
                "port_id": "icacontroller-uratom-0-withdrawal",
                "channel_id": "channel-2"
            },
            "connection_hops": [
                "connection-618"
            ],
            "version": "{\"version\":\"ics27-1\",\"controller_connection_id\":\"connection-0\",\"host_connection_id\":\"connection-618\",\"address\":\"cosmos1tne2mwtwgeeh2hr4vw9vt0uj5s4dln5qga7f7llmmqrydewwafds6zmjq4\",\"encoding\":\"proto3\",\"tx_type\":\"sdk_multi_msg\"}",
            "port_id": "icahost",
            "channel_id": "channel-370"
        },
        {
            "state": "STATE_OPEN",
            "ordering": "ORDER_ORDERED",
            "counterparty": {
                "port_id": "icacontroller-uratom-0-delegation",
                "channel_id": "channel-1"
            },
            "connection_hops": [
                "connection-618"
            ],
            "version": "{\"version\":\"ics27-1\",\"controller_connection_id\":\"connection-0\",\"host_connection_id\":\"connection-618\",\"address\":\"cosmos1kzlrmxw3h2n4uzuv73m33cfw7xt7qjf3hlqx33ulc02e9dhxu46qgfxg9l\",\"encoding\":\"proto3\",\"tx_type\":\"sdk_multi_msg\"}",
            "port_id": "icahost",
            "channel_id": "channel-371"
        }
    ],
    "pagination": {
        "next_key": "L3BvcnRzL3RyYW5zZmVyL2NoYW5uZWxzL2NoYW5uZWwtMTI2",
        "total": "528"
    },
    "height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
