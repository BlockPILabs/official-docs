---
description: Return all [DelegatedStake].
---

# suix\_getStakes

#### **Parameters:**

**owner< SuiAddress >** -

#### **Returns:**

Vec<\[ DelegatedStake ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getStakes",
  "params": [
    "0xb5387b29a731d26d98108d7abc4902107d7d6a8e0f8fea6fda5488462e58724c"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": [],
    "id": 1
}
```
{% endcode %}
