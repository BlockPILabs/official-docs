---
description: >-
  Returns changes in block for given block height or hash. You can also use
  finality param to return latest block details.
---

# Changes in Block

* method: `EXPERIMENTAL_changes_in_block`
* params:
  * [`finality`](https://docs.near.org/api/rpc/setup#using-finality-param) _OR_ [`block_id`](https://docs.near.org/api/rpc/setup#using-block_id-param)

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "EXPERIMENTAL_changes_in_block",
  "params": {
    "finality": "final"
  }
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "block_hash": "81k9ked5s34zh13EjJt26mxw5npa485SY4UNoPi6yYLo",
    "changes": [
      {
        "type": "account_touched",
        "account_id": "lee.testnet"
      },
      {
        "type": "contract_code_touched",
        "account_id": "lee.testnet"
      },
      {
        "type": "access_key_touched",
        "account_id": "lee.testnet"
      }
    ]
  },
  "id": "dontcare"
}
```
{% endcode %}
