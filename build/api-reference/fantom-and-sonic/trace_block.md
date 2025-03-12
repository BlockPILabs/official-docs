---
description: Returns traces created at given block.
---

# trace\_block

#### **Parameters:**

**Quantity |Tag** - Integer of a block number, or the string 'earliest', 'latest' or 'pending'.

#### **Returns:**

**Array** - Block traces

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://https://fantom.blockpi.network/v1/rpc/<your-api-key> -X POST -H "Content-Type: application/json" -d '{"method":"trace_block","params":["latest"],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":{as described above}
}
```
{% endcode %}
