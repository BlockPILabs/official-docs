---
description: >-
  Returns the current price of gas in wei. If minimum gas price is enforced by
  setting the --price-limit flag, this endpoint will return the value defined by
  this flag as minimum gas price.
---

# eth\_gasPrice

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the current gas price in wei.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://monad.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": "0xc1b710800",
    "id": 18902699
}
```
{% endcode %}
