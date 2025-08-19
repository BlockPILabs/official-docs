---
description: Return the total coin balance for all coin type, owned by the address owner.
---

# suix\_getAllBalances

#### **Parameters:**

**owner< SuiAddress >** - The owner's Sui address

#### **Returns:**

Vec<\[ Balance ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getAllBalances",
  "params": [
    "0x94f1a597b4e8f709a396f7f6b1482bdcd65a673d111e49286c527fab7c2d0961"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "[ ]"
}
```
{% endcode %}
