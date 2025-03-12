---
description: Returns an estimate of the gas required for a L1 to L2 transaction.
---

# zks\_estimateGasL1ToL2

#### **Parameters:**

**request-CallRequest**, The zkSync transaction request for which the gas fee is estimated.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "id":2, "method": "zks_estimateGasL1ToL2", "params": [ { "from": "0x1111111111111111111111111111111111111111", "to":"0x2222222222222222222222222222222222222222", "data": "0xffffffff" } ] }'

// Result
{
  "jsonrpc": "2.0",
  "result": "0x25f64db",
  "id": 2
}


```
{% endcode %}
