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
curl https://cronos.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x469dfe519740073a1ce424b3eeaf136b4cb29d575e9a155266d7cf117b618844"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xc5b61f4b50a85f5f26358033e64c85df7f1c36e89323c868194b50c5f2ce949f",
        "blockNumber": "0x6c3a74",
        "from": "0xf690181fa630f3895643bbe8b0fccf90330ddeeb",
        "gas": "0xe315",
        "gasPrice": "0x45eef6aeecf",
        "hash": "0x469dfe519740073a1ce424b3eeaf136b4cb29d575e9a155266d7cf117b618844",
        "input": "0x095ea7b30000000000000000000000008d13982c702fe7c6537529986df67dabeafc4c19ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "nonce": "0x4",
        "to": "0x2d03bece6747adc00e1a131bba1469c15fd11e03",
        "transactionIndex": "0x2",
        "value": "0x0",
        "type": "0x0",
        "v": "0x56",
        "r": "0xe083bf53e36089c6ef3dff23bc97f89aa8647b96bde2c4c62f111c99d0fe875e",
        "s": "0x602bb22c9ced4d07b1a709fbc3074c3a939fc3a91e9cbce7373b4b399fa67669"
    }
}
```
{% endcode %}
