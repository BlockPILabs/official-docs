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
curl https://unichain.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x426920cdcd5cda439509724ed7c2aa55b8de461eb609406e94746bbbc9dddfd6"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xe864abc1db10e20baba27b12aa155975decab151576ef76cc6f278e30709e3ff",
        "blockNumber": "0x2ab912",
        "from": "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0001",
        "gas": "0xf4240",
        "gasPrice": "0x0",
        "hash": "0xc02b19353b9793a3c8841a9d70ef7534df584eb3efa8b332c23bbeb314053f9c",
        "input": "0x440a5e20000007d0000dbba000000000000000000000000067186620000000000069b0cf00000000000000000000000000000000000000000000000000000000132354e4000000000000000000000000000000000000000000000000000000000000009233b80ed624166a9d2fa2d436d6a097fbd0affc9f6636d3395516139e5ce714400000000000000000000000004ab3387810ef500bfe05a49dc53a44c222cbab3e",
        "nonce": "0x2ab911",
        "to": "0x4200000000000000000000000000000000000015",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x7e",
        "v": "0x0",
        "r": "0x0",
        "s": "0x0",
        "sourceHash": "0xe9758e90f771754d2ac886ef7c747e7d69041eb33a332138f1e2674c7ab4d4e5",
        "mint": "0x0",
        "depositReceiptVersion": "0x1"
    }
}
```
{% endcode %}
