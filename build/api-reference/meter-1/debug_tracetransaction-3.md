---
description: Returns an array of EIP-2718 binary-encoded transactions.
---

# debug\_getRawTransaction

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

#### **Returns:**

**String**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://monad.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_getRawTransaction","params":["0x47d261f2d7993288c06fd97b5411c0ca9ea341b93fe83eb37ff77f3787bd601b"],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": -
}
```
{% endcode %}
