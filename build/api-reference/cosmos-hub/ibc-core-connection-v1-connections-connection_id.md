---
description: Connection queries an IBC connection end.
---

# /ibc/core/connection/v1/connections/{connection\_id}

#### **Parameters:**

**connection\_id - string**, connection unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/connection/v1/connections/connection-188

// Result
{
    "connection": {
        "client_id": "07-tendermint-142",
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
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
