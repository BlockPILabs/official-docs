---
description: Status queries the status of an IBC client.
---

# /ibc/core/client/v1/client\_status/{client\_id}

#### **Parameters:**

**client\_id - string**, client unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/client/v1/client_status/07-tendermint-0

// Result
{
    "status": "Expired"
}
```
{% endcode %}
