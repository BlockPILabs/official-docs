---
description: >-
  Returns the number of hashes per second that the node is mining with. Only
  applicable when the node is mining.
---

# eth\_hashrate

#### **Parameters:**

none

#### **Returns:**

**QUANTITY** - number of hashes per second.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_hashrate","params":[],"id":71}'

// Result
{
    "jsonrpc":"2.0",
    "id":71,
    "result":"0x0"
}
```
{% endcode %}
