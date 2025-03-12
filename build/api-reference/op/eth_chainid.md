---
description: >-
  Returns the currently configured chain id, a value used in replay-protected
  transaction signing as introduced by EIP-155.
---

# eth\_chainId

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the current chain id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}'

// Result
{
  "jsonrpc":"2.0",
  "id":1,
  "result":"0xa"
}
```
{% endcode %}
