---
description: >-
  Returns the hash of the best (tip) block in the most-work fully-validated
  chain.
---

# getbestblockhash

#### **Parameters:**

None

#### **Returns:**

string, the block hash, hex-encoded

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getbestblockhash", "params": []}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "000000000000000000020b1823dfd1bd92b9ae7821a38e63ac24e06db765d7db"
}
```
{% endcode %}
