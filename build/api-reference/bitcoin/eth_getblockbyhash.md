---
description: >-
  Returns the height of the most-work fully-validated chain.  The genesis block
  has height 0
---

# getblockcount

#### **Parameters:**

**None**

#### **Returns:**

numeric The current block count

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getblockcount", "params": []}'

// Result
{
    "result": 910819,
    "error": null,
    "id": "1"
}
```
{% endcode %}
