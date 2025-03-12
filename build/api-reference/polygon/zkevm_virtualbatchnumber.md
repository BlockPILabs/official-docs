---
description: Returns the latest virtual batch number
---

# zkevm\_virtualBatchNumber

#### **Parameters:**

**None**

**Returns**

**Boolean** - the latest virtual batch number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon-zkevm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "zkevm_virtualBatchNumber",
    "params": [],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x56b7"
}
```
{% endcode %}
