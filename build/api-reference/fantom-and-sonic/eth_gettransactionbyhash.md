---
description: Returns the information about a transaction requested by transaction hash.
---

# eth\_getTransactionByHash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

#### **Returns:**

**Object** - A transaction object, or null when no transaction was found:

* **blockHash: DATA, 32 Bytes** - hash of the block where this transaction was in.
* **blockNumber: QUANTITY** - block number where this transaction was in.
* **from: DATA, 20 Bytes** - address of the sender.
* **gas: QUANTITY** - gas provided by the sender.
* **gasPrice: QUANTITY** - gas price provided by the sender in Wei.
* **hash: DATA, 32 Bytes** - hash of the transaction.
* **input: DATA** - the data send along with the transaction.
* **nonce: QUANTITY** - the number of transactions made by the sender prior to this one.
* **to: DATA, 20 Bytes** - address of the receiver. null when its a contract creation transaction.
* **transactionIndex: QUANTITY** - integer of the transactions index position in the block.
* **value: QUANTITY** - value transferred in Wei.
* **v: QUANTITY** - ECDSA recovery id
* **r: DATA, 32 Bytes** - ECDSA signature r
* **s: DATA, 32 Bytes** - ECDSA signature s

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xee2c000e6f553af6209543b7e1ded2fc7bc4ce2ca65ec8b2e04e9c59c65f4dba"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x0002cd1b00000002c49530f0cb42883a2ba875674f7d6c9731754cb2fa23d2e0",
        "blockNumber": "0x3315cf2",
        "from": "0x363dcc5df47f1f32c3a3f16da250b7d6cec659d5",
        "gas": "0x895440",
        "gasPrice": "0x773594000",
        "hash": "0xee2c000e6f553af6209543b7e1ded2fc7bc4ce2ca65ec8b2e04e9c59c65f4dba",
        "input": "0xa0712d68000000000000000000000000000000000000000000000000000000000000004d",
        "nonce": "0x1",
        "to": "0x97faab98f1a9e5c803c43a6293759fcc7ed000b9",
        "transactionIndex": "0x3",
        "value": "0x0",
        "type": "0x0",
        "v": "0x218",
        "r": "0x8cad2c225a3b98c18482d72b529fed45cfe760dcb8428cb124660cc347b5efeb",
        "s": "0x3c7afaa932c4598d1e1340e7a11b62099ecffc9454eb1c4c39c4a4d7a019a60"
    }
}
```
{% endcode %}
