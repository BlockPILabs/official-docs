---
description: >-
  Returns the address of the testnet paymaster: the paymaster that is available
  on testnets and enables paying fees in ERC-20 compatible tokens.
---

# zks\_getTestnetPaymaster

**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getTestnetPaymaster", "params": [ 5187 ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": "0x8f0ea1312da29f17eabeb2f484fd3c112cccdd63",
  "id": 1
}
```
{% endcode %}
