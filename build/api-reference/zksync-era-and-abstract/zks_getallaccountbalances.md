---
description: Returns all balances for confirmed tokens given by an account address.
---

# zks\_getAllAccountBalances

#### **Parameters:**

**address-Address**, The account address.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getAllAccountBalances", "params": [ "0x98E9D288743839e96A8005a6B51C770Bbf7788C0" ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "0x0000000000000000000000000000000000000000": "0x2fbd72a1121b3100"
  },
  "id": 2
}

```
{% endcode %}
