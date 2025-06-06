---
description: >-
  Returns 'true' if the provided block number is already connected to a batch
  that was already virtualized, otherwise 'false'
---

# zkevm\_isBlockVirtualized

#### **Parameters:**

**String** - hash of block

**Boolean** - if `true` it returns the full transaction objects, if `false`, only the hashes of the transactions; defaults to `false`

**Returns**

**Boolean** - result of virtualized

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon-zkevm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "zkevm_isBlockVirtualized",
    "params": [
        "0x2"
    ],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": true
}
```
{% endcode %}
