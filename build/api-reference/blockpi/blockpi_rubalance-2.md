---
description: >-
  Using any existing key to query the consumed RUs within the time period for
  corresponding endpoint.
---

# blockpi\_ruConsumed

#### **Parameters:**

**apikey --** any API key that the users already created in their account.

**days --** "1", "3", or"7"

#### **Returns:**

**cost --** the consumed RUs within the time period for corresponding endpoint.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl  https://api.blockpi.io/openapi/v1/rpc -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "blockpi_ruConsumed",
    "params": [
        {
            "apiKey": "0fea34a6584b71e1df7794c4b2b405a3dddeea8a",
            "days": "3" 
        }
    ],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "cost": 0
    }
}
```
{% endcode %}
