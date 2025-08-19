---
description: Return the total coin balance for one coin type, owned by the address owner.
---

# suix\_getBalance

#### **Parameters:**

**owner< SuiAddress >** - The owner's Sui address\
**coin\_type< string >** - Optional type names for the coin (e.g., 0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC), default to 0x2::sui::SUI if not specified.

#### **Returns:**

Balance< Balance >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getBalance",
  "params": [
    "0x51ceab2edc89f74730e683ebee65578cb3bc9237ba6fca019438a9737cf156ae",
    "0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "coinType": "0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC",
        "coinObjectCount": 0,
        "totalBalance": "0",
        "lockedBalance": {}
    },
    "id": 1
}
```
{% endcode %}
