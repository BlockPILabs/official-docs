---
description: Returns the proof-of-work difficulty as a multiple of the minimum difficulty.
---

# getdifficulty

#### **Parameters:**

**None**

#### **Returns:**

numeric, the proof-of-work difficulty as a multiple of the minimum difficulty.

### Examples

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getdifficulty", "params": [ ]}'

// Result
{
    "result": 129435235580344.8,
    "error": null,
    "id": "1"
}
```
{% endcode %}
