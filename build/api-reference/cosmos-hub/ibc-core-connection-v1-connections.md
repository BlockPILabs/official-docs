---
description: Connections queries all the IBC connections of a chain.
---

# /ibc/core/connection/v1/connections

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/connection/v1/connections

// Result
{
    "connections": [
        {
            "id": "connection-0",
            "client_id": "07-tendermint-1",
            "versions": [
                {
                    "identifier": "1",
                    "features": [
                        "ORDER_ORDERED",
                        "ORDER_UNORDERED"
                    ]
                }
            ],
            "state": "STATE_TRYOPEN",
            "counterparty": {
                "client_id": "07-tendermint-0",
                "connection_id": "connection-0",
                "prefix": {
                    "key_prefix": "aWJj"
                }
            },
            "delay_period": "0"
        },
        {
            "id": "connection-1",
            "client_id": "07-tendermint-1",
            "versions": [
                {
                    "identifier": "1",
                    "features": [
                        "ORDER_ORDERED",
                        "ORDER_UNORDERED"
                    ]
                }
            ],
            "state": "STATE_OPEN",
            "counterparty": {
                "client_id": "07-tendermint-0",
                "connection_id": "connection-0",
                "prefix": {
                    "key_prefix": "aWJj"
                }
            },
            "delay_period": "0"
        },
        ......
     ],
    "pagination": {
        "next_key": "L2Nvbm5lY3Rpb24tMTg5",
        "total": "784"
    },
    "height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}    
```
{% endcode %}
