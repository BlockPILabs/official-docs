---
description: Returns the latest L1 batch number.
---

# zks\_L1ChainId

**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_L1ChainId", "params": [ ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": "0x1",
  "id": 1
}
```
{% endcode %}
