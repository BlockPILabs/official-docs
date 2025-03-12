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
curl https://base.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x57294047f5f7b7eb9aec7a2b414b4fffe89598b26025c9c4bab9d8d363e3ac82"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x7896799aa9972636ce6621f5099fb0b541406337e33f6b16d733ebfec9f68fe7",
        "blockNumber": "0x5f1dae",
        "from": "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0001",
        "gas": "0xf4240",
        "gasPrice": "0x0",
        "hash": "0x57294047f5f7b7eb9aec7a2b414b4fffe89598b26025c9c4bab9d8d363e3ac82",
        "input": "0x015d8eb900000000000000000000000000000000000000000000000000000000008ced53000000000000000000000000000000000000000000000000000000006497a804000000000000000000000000000000000000000000000000000000000048588ad95d6c1b009e9e7f1b18b1ea2f9dc3dfa2588b67afb757f9355f5ea9a11655f5000000000000000000000000000000000000000000000000000000000000000500000000000000000000000073b4168cc87f35cc239200a20eb841cded23493b000000000000000000000000000000000000000000000000000000000000083400000000000000000000000000000000000000000000000000000000000f4240",
        "nonce": "0x5f1dad",
        "to": "0x4200000000000000000000000000000000000015",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x7e",
        "v": "0x0",
        "r": "0x0",
        "s": "0x0",
        "sourceHash": "0x4921d9cceeabad2354630ae0cb0a1302df655e9269772c8380bf322b820537fd",
        "mint": "0x0"
    }
}
```
{% endcode %}
