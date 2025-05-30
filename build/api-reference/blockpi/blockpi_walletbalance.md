---
description: >-
  Using any existing key to query the currently wallet balance of the account
  which owns the api key.
---

# blockpi\_walletBalance

#### **Parameters:**

**apikey** -- any API key that the users already created in their account.

#### **Returns:**

**balance** -- the remaining wallet balance of the account in dollar.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl  https://api.blockpi.io/openapi/v1/rpc -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "blockpi_walletBalance",
    "params": [
        {
            "apiKey": "60794194a000ijb35af7e1180i311a26297a3b0w" 
        }
    ],
    "id": 1
}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "balance": 0
    }
}
```
{% endcode %}
