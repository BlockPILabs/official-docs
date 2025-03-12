---
description: >-
  Returns code changes made when deploying a contract. Change is returned is a
  base64 encoded WASM file.
---

# View contract code changes

* method: `EXPERIMENTAL_changes`
* params:
  * `changes_type`: `contract_code_changes`
  * `account_ids`: `["example.testnet"]`,
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
  "method": "EXPERIMENTAL_changes",
  "params": {
    "changes_type": "contract_code_changes",
    "account_ids": ["dev-1602714453032-7566969"],
    "block_id": 20046655
  }
}'

// Result
{
    "error": {
        "name": <ERROR_TYPE>,
        "cause": {
            "info": {..},
            "name": <ERROR_CAUSE>
        },
        "code": -32000,
        "data": String,
        "message": "Server error",
    },
    "id": "dontcare",
    "jsonrpc": "2.0"
}
```
{% endcode %}
