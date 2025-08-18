---
description: >-
  Using any existing key to query the consumed RUs within the time period for
  corresponding endpoint.
---

# blockpi\_packageExpiration

#### **Parameters:**

**apikey --** any API key that the users already created in their account.

#### **Returns:**

**Object** - A details object, or null:

* ruTotalAmoun&#x74;**: QUANTITY**  - Total RU amount of the RU package.
* ruLeftAmoun&#x74;**: QUANTITY** - Available RU amount left of the RU package.
* skuNam&#x65;**: DATA** - RU package name.
* expireTim&#x65;**: QUANTITY** - UTC number when the package expires.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl  https://api.blockpi.io/openapi/v1/rpc -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "blockpi_packageExpiration",
    "params": [
        {
            "apiKey": "0fea34a6584b71e1df7794c4b2b405a3dddeea8a"
        }
    ],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "details": [
            {
                "ruTotalAmount": 4000000000,
                "ruLeftAmount": 3687787426,
                "skuName": "Startup Premium",
                "expireTime": 1761451280832
            }
        ],
        "totalCount": 1
    }
}
```
{% endcode %}
