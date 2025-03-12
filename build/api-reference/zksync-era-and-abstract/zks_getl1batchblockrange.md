---
description: >-
  Returns the range of blocks contained within a batch given by batch number.
  The range is given by beginning/end block numbers in hexadecimal.
---

# zks\_getL1BatchBlockRange

**Parameters:**

**batch-L1BatchNumber**, The layer 1 batch number.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getConfirmedTokens", "params": [ 12345 ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": ["0x116fec", "0x117015"],
  "id": 1
}



```
{% endcode %}
