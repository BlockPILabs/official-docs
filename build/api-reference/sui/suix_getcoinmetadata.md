---
description: Return metadata(e.g., symbol, decimals) for a coin
---

# suix\_getCoinMetadata

#### **Parameters:**

**coin\_type< string >** - Type name for the coin (e.g., 0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC)

#### **Returns:**

SuiCoinMetadata< SuiCoinMetadata >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getCoinMetadata",
  "params": [
    "0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": null,
    "id": 1
}
```
{% endcode %}
