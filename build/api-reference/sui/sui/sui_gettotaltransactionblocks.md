---
description: Return the total number of transaction blocks known to the server.
---

# sui\_getTotalTransactionBlocks

#### **Parameters:**

**None**

#### **Returns:**

BigInt< BigInt\_for\_uint64 >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getTotalTransactionBlocks",
  "params": []
}'

// Result
{
    "jsonrpc": "2.0",
    "result": "86440532",
    "id": 1
}
```
{% endcode %}
