---
description: Returns the batch number connected to the block
---

# zkevm\_batchNumberByBlockNumber

#### **Parameters:**

An array of strings&#x20;

**String** - the hex representation of the block's height

#### **Returns:**

**String** - the hex representation of latest batch number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon-zkevm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
'{
    "jsonrpc": "2.0",
    "method": "zkevm_batchNumberByBlockNumber",
    "params": [
        "0x2"
    ],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x4"
}
```
{% endcode %}
