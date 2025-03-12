---
description: >-
  list the exact details of all the transactions currently pending for inclusion
  in the next block(s), as well as the ones that are being scheduled for future
  execution only.
---

# txpool\_content

#### **Parameters:**

None

#### Returns:

**array** - list of pending and queued transations, with each having the following fields:

**pending** - Array of transaction objects, with following fields:

* **blockHash** - Hash of the block where this transaction was in, null here.
* **blockNumber** - Block number where this transaction was added encoded as a hexadecimal, null here.
* **from** - Address of the sender.
* **gas** - The total amount of gas units used in the transaction.
* **gasPrice** - The total amount in wei the sender is willing to pay for the transaction.
* **hash** - Hash of the transaction.
* **input** - Encoded transaction input data.
* **nonce** - Number of transactions the sender has sent till now.
* **r** - ECDSA signature r.
* **s** - ECDSA signature s.
* **to** - Address of the receiver. null when its a contract creation transaction.
* **transactionIndex** - Integer of the transactions index position in the block encoded as a hexadecimal.
* **type** - A number between 0 and 0x7f, for a total of 128 possible transaction types.
* **v** - ECDSA recovery id encoded as a hexadecimal.
* **value** - Value transferred in Wei encoded as a hexadecimal.

**queued** - Array of transaction objects, with following fields:

* **accesslist** - A list of addresses and storage keys that the transaction plans to access, introduced in EIP-2929.
* **blockHash** - Hash of the block where this transaction was in, null here.
* **blockNumber** - Block number where this transaction was added encoded as a hexadecimal, null here.
* **chainId** - The current network/chain ID, used to sign repplay-protected transaction introduced in EIP-155.
* **from** - Address of the sender.
* **gas**- The total amount of gas units used in the transaction.
* **gasPrice** - The total amount in wei the sender is willing to pay for the transaction.
* **hash** - Hash of the transaction.
* **input** - Encoded transaction input data.
* **maxFeePerGas** - The maximum amount of gas willing to be paid for the transaction.
* **maxPriorityFeePerGas** - The maximum amount of gas to be included as a tip to the miner.
* **nonce** - Number of transactions the sender has sent till now.
* **r** - ECDSA signature r.
* **s** - ECDSA signature s.
* **to** - Address of the receiver. null when its a contract creation transaction.
* **transactionIndex** - Integer of the transactions index position in the block encoded as a hexadecimal.
* **type** - A number between 0 and 0x7f, for a total of 128 possible transaction types.
* **v** - ECDSA recovery id encoded as a hexadecimal.
* **value** - Value transferred in Wei encoded as a hexadecimal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_content","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {as described above}
}
```
{% endcode %}
