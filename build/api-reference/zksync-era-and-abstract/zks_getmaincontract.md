---
description: Returns the address of the zkSync Era contract.
---

# zks\_getMainContract

**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getMainContract", "params": [ ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": "0x32400084c286cf3e17e7b677ea9583e60a000324",
  "id": 1
}
```
{% endcode %}
