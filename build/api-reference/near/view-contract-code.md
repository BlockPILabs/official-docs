---
description: >-
  Returns the contract code (Wasm binary) deployed to the account. Please note
  that the returned code will be encoded in base64.
---

# View contract code

* method: `query`
* params:
  * `request_type`: `view_code`
  * [`finality`](https://docs.near.org/api/rpc/setup#using-finality-param) _OR_ [`block_id`](https://docs.near.org/api/rpc/setup#using-block_id-param)
  * `account_id`: `"guest-book.testnet"`,

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
    "request_type": "view_code",
    "finality": "final",
    "account_id": "guest-book.testnet"
  }
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "code_base64": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
    "hash": "7KoFshMQkdyo5iTx8P2LbLu9jQpxRn24d27FrKShNVXs",
    "block_height": 17814234,
    "block_hash": "GT1D8nweVQU1zyCUv399x8vDv2ogVq71w17MyR66hXBB"
  },
  "id": "dontcare"
}
```
{% endcode %}
