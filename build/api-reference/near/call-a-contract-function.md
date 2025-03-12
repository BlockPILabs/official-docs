---
description: Allows you to call a contract method as a view function.
---

# Call a contract function

* method: `query`
* params:
  * `request_type`: `call_function`
  * [`finality`](https://docs.near.org/api/rpc/setup#using-finality-param) _OR_ [`block_id`](https://docs.near.org/api/rpc/setup#using-block_id-param)
  * `account_id`: _`"example.testnet"`_
  * `method_name`: `name_of_a_example.testnet_method` (example [`view` methods](https://github.com/near/core-contracts/blob/master/staking-pool/src/lib.rs#L317)
  * `args_base64`: `method_arguments_base_64_encoded`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "query",
  "params": {
    "request_type": "call_function",
    "finality": "final",
    "account_id": "dev-1588039999690",
    "method_name": "get_account_staked_balance",
    "args_base64": "eyJhY2NvdW50X2lkIjoiZGV2LTE1ODgwMzk5OTk2OTAifQ=="
  }
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "result": [48],
    "logs": [],
    "block_height": 17817336,
    "block_hash": "4qkA4sUUG8opjH5Q9bL5mWJTnfR4ech879Db1BZXbx6P"
  },
  "id": "dontcare"
}
```
{% endcode %}
