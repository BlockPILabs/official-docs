---
description: ClientConnections queries the connection paths associated with a client state.
---

# /ibc/core/connection/v1/client\_connections/{client\_id}

#### **Parameters:**

**client\_id - string**, client identifier associated with a connection

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/connection/v1/client_connections/07-tendermint-0

// Result
{
    "connection_paths": [
        "connection-560",
        "connection-561",
        "connection-562"
    ],
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
