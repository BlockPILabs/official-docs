---
description: Returns account changes from transactions in a given account.
---

# View account changes

* method: `EXPERIMENTAL_changes`
* params:
  * `changes_type`: `account_changes`
  * `account_ids`: \[`"example.testnet"`]
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
    "changes_type": "account_changes",
    "account_ids": ["your_account.testnet"],
    "block_id": 19703467
  }
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "block_hash": "6xsfPSG89s6fCMShxxxQTP6D4ZHM9xkGCgubayTDRzAP",
    "changes": [
      {
        "cause": {
          "type": "transaction_processing",
          "tx_hash": "HLvxLKFM7gohFSqXPp5SpyydNEVpAno352qJJbnddsz3"
        },
        "type": "account_update",
        "change": {
          "account_id": "your_account.testnet",
          "amount": "499999959035075000000000000",
          "locked": "0",
          "code_hash": "11111111111111111111111111111111",
          "storage_usage": 182,
          "storage_paid_at": 0
        }
      },
      {
        "cause": {
          "type": "receipt_processing",
          "receipt_hash": "CPenN1dp4DNKnb9LiL5hkPmu1WiKLMuM7msDjEZwDmwa"
        },
        "type": "account_update",
        "change": {
          "account_id": "your_account.testnet",
          "amount": "499999959035075000000000000",
          "locked": "0",
          "code_hash": "11111111111111111111111111111111",
          "storage_usage": 264,
          "storage_paid_at": 0
        }
      }
    ]
  },
  "id": "dontcare"
}
```
{% endcode %}
