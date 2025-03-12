---
description: Fetches a receipt by it's ID (as is, without a status or execution outcome)
---

# Receipt by ID

* method: `EXPERIMENTAL_receipt`
* params:
  * `receipt_id` _(see_ [_NearBlocks Explorer_](https://testnet.nearblocks.io/) _for a valid receipt id)_

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "EXPERIMENTAL_receipt",
  "params": { "receipt_id": "2EbembRPJhREPtmHCrGv3Xtdm3xoc5BMVYHm3b2kjvMY" }
}'

// Result
{
  "id": "dontcare",
  "jsonrpc": "2.0",
  "result": {
    "predecessor_id": "bohdan.testnet",
    "receipt": {
      "Action": {
        "actions": [
          {
            "Transfer": {
              "deposit": "1000000000000000000000000"
            }
          }
        ],
        "gas_price": "103000000",
        "input_data_ids": [],
        "output_data_receivers": [],
        "signer_id": "bohdan.testnet",
        "signer_public_key": "ed25519:DhC7rPNTBwWJtmVXs1U1SqJztkn9AWbj6jCmQtkrg3TA"
      }
    },
    "receipt_id": "2EbembRPJhREPtmHCrGv3Xtdm3xoc5BMVYHm3b2kjvMY",
    "receiver_id": "frol.testnet"
  }
}
```
{% endcode %}
