---
description: >-
  Queries status of a transaction by hash, returning the final transaction
  result and details of all receipts.
---

# Transaction Status with Receipts

* method: `EXPERIMENTAL_tx_status`
* params:
  * `tx_hash` _(see_ [_NearBlocks Explorer_](https://testnet.nearblocks.io/) _for a valid transaction hash)_
  * `sender_account_id` _(used to determine which shard to query for transaction)_
  * \[Optional] `wait_until`: the required minimal execution level. Read more [here](https://docs.near.org/api/rpc/transactions#tx-status-result). The default value is `EXECUTED_OPTIMISTIC`.

A Transaction status request with `wait_until != NONE` will wait until the transaction appears on the blockchain. If the transaction does not exist, the method will wait until the timeout is reached. If you only need to check whether the transaction exists, use `wait_until = NONE`, it will return the response immediately.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "EXPERIMENTAL_tx_status",
  "params": {
    "tx_hash": "HEgnVQZfs9uJzrqTob4g2Xmebqodq9waZvApSkrbcAhd",
    "sender_account_id": "bowen",
    "wait_until": "EXECUTED"
  }
}'

// Result
{
  "id": "123",
  "jsonrpc": "2.0",
  "result": {
    "final_execution_status": "FINAL",
    "receipts": [
      {
        "predecessor_id": "bowen",
        "receipt": {
          "Action": {
            "actions": [
              {
                "FunctionCall": {
                  "args": "eyJhbW91bnQiOiIxMDAwIiwicmVjZWl2ZXJfaWQiOiJib3dlbiJ9",
                  "deposit": "0",
                  "gas": 100000000000000,
                  "method_name": "transfer"
                }
              }
            ],
            "gas_price": "186029458",
            "input_data_ids": [],
            "output_data_receivers": [],
            "signer_id": "bowen",
            "signer_public_key": "ed25519:2f9Zv5kuyuPM5DCyEP5pSqg58NQ8Ct9uSRerZXnCS9fK"
          }
        },
        "receipt_id": "FXMVxdhSUZaZftbmPJWaoqhEB9GrKB2oqg9Wgvuyvom8",
        "receiver_id": "evgeny.lockup.m0"
      },
      ......
```
{% endcode %}
