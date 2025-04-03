---
description: >-
  Returns a fee per gas that is an estimate of how much you can pay as a
  priority fee, or "tip", to get a transaction included in the current block.
---

# eth\_maxPriorityFeePerGas

#### **Parameters:**

None

#### **Returns:**

**QUANTITY**  - the estimated priority fee per gas.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://t3rn.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_maxPriorityFeePerGas","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x0"
}
```
{% endcode %}
