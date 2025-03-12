---
description: Return the validator APY
---

# suix\_getValidatorsApy

#### **Parameters:**

None

#### **Returns:**

ValidatorApys< ValidatorApys >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getValidatorsApy",
  "params": []
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "apys": [
            {
                "address": "0x11ec7353e9e08ed4ca13b935ad930a2f937112736aec5eedd08c95cc5cd4c264",
                "apy": 0.03085651630217174
            },
```
{% endcode %}
