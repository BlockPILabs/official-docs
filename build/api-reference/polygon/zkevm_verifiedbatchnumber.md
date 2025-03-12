---
description: Returns the latest verified batch number
---

# zkevm\_verifiedBatchNumber

#### **Parameters:**

**None**

**Returns**

**Boolean** - the latest verified batch number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon-zkevm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "zkevm_verifiedBatchNumber",
    "params": [],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x568a"
}
```
{% endcode %}
