---
description: Returns the latest block number that is connected to the latest batch verified
---

# zkevm\_consolidatedBlockNumber

#### **Parameters:**

**None**

#### **Returns:**

**String** - the hex representation of latest block number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon-zkevm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
'{
    "jsonrpc": "2.0",
    "method": "zkevm_consolidatedBlockNumber",
    "params": [],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x7ea6b"
}
```
{% endcode %}
