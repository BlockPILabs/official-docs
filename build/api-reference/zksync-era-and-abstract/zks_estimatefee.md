---
description: Returns the fee for the transaction.
---

# zks\_estimateFee

#### **Parameters:**

**request-CallRequest**, The zkSync transaction request for which the fee is estimated.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "id":2, "method": "zks_estimateFee", "params": [ { "from": "0x1111111111111111111111111111111111111111", "to":"0x2222222222222222222222222222222222222222", "data": "0xffffffff" } ] }'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "gas_limit": "0x156c00",
    "gas_per_pubdata_limit": "0x143b",
    "max_fee_per_gas": "0xee6b280",
    "max_priority_fee_per_gas": "0x0"
  },
  "id": 2
}

```
{% endcode %}
