---
description: >-
  Returns the state change details of a contract based on the key prefix
  (encoded to base64). Pass an empty string for this param if you would like to
  return all state changes.
---

# View contract state changes

* method: `EXPERIMENTAL_changes`
* params:
  * `changes_type`: `data_changes`
  * `account_ids`: `["example.testnet"]`,
  * `key_prefix_base64`: `"base64 encoded key value"`,
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
    "changes_type": "data_changes",
    "account_ids": ["guest-book.testnet"],
    "key_prefix_base64": "",
    "block_id": 19450732
  }
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "block_hash": "6U8Yd4JFZwJUNfqkD4KaKgTKmpNSmVRTSggpjmsRWdKY",
    "changes": [
      {
        "cause": {
          "type": "receipt_processing",
          "receipt_hash": "9ewznXgs2t7vRCssxW4thgaiwggnMagKybZ7ryLNTT2z"
        },
        "type": "data_update",
        "change": {
          "account_id": "guest-book.testnet",
          "key_base64": "bTo6Mzk=",
          "value_base64": "eyJwcmVtaXVtIjpmYWxzZSwic2VuZGVyIjoiZmhyLnRlc3RuZXQiLCJ0ZXh0IjoiSGkifQ=="
        }
      },
      {
        "cause": {
          "type": "receipt_processing",
          "receipt_hash": "9ewznXgs2t7vRCssxW4thgaiwggnMagKybZ7ryLNTT2z"
        },
        "type": "data_update",
        "change": {
          "account_id": "guest-book.testnet",
          "key_base64": "bTpsZW4=",
          "value_base64": "NDA="
        }
      }
    ]
  },
  "id": "dontcare"
}
```
{% endcode %}
