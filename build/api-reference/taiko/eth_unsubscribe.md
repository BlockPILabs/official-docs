---
description: >-
  Subscriptions are cancelled with a regular RPC call with eth_unsubscribe as a
  method and the subscription id as the first parameter. It returns a bool
  indicating if the subscription was cancelled.
---

# eth\_unsubscribe

#### **Parameters:**

**SUBSCRIPTION ID**

#### **Returns:**

**UNSUBSCRIBED FLAG** - true if the subscription was cancelled successful.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://taiko-hekla.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_unsubscribe","params":["0x9cef478923ff08bf67fde6c64013158d"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": ture
}
```
{% endcode %}
