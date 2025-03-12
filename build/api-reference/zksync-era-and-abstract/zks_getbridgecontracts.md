---
description: Returns L1/L2 addresses of default bridges.
---

# zks\_getBridgeContracts

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getBridgeContracts", "params": [ ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "l1Erc20DefaultBridge": "0x57891966931eb4bb6fb81430e6ce0a03aabde063",
    "l2Erc20DefaultBridge": "0x11f943b2c77b743ab90f4a0ae7d5a4e7fca3e102"
  },
  "id": 1
}



```
{% endcode %}
