---
description: Returns gas price for a specific block_height or block_hash.
---

# Gas Price

* Using `[null]` will return the most recent block's gas price.
* method: `gas_price`
* params: `[block_height]`, `["block_hash"]`, or `[null]`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "gas_price",
  "params": [17824600]
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "gas_price": "100000000"
  },
  "id": "dontcare"
}
```
{% endcode %}
