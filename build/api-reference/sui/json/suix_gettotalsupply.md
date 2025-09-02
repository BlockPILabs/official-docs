---
description: Return total supply for a coin
---

# suix\_getTotalSupply

#### **Parameters:**

**coin\_type< string >** - Type name for the coin (e.g., 0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC)

#### **Returns:**

Supply< Supply >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getTotalSupply",
  "params": [
    "0x2::sui::SUI"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "value": "10000000000000000000"
    },
    "id": 1
}
```
{% endcode %}
