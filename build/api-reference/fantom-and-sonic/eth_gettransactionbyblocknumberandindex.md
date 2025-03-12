---
description: >-
  Returns the information about a transaction requested by Block number and
  index.
---

# eth\_getTransactionByBlockNumberAndIndex

#### **Parameters:**

**QUANTITY|TAG** - Integer block number encoded as a hexadecimal, or the string 'latest', 'earliest' or 'pending'.

**QUANTITY** - A hex of the integer representing the position in the block.

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
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0xF2F8D7", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x0000755e0000040317b66f1b4b31d6e7544b163b9ca7ff0f6ccf459f2dd38a5f",
        "blockNumber": "0xf2f8d7",
        "from": "0x060c1838103661acb15362eee0bc07f3d51cd4b1",
        "gas": "0x445c0",
        "gasPrice": "0xe8d4a51000",
        "hash": "0x84ec79383856b2d900dc42550a1aa431a0d093b7bdfe0559e10acc22566e66fa",
        "input": "0xb3d16931000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000030000000000000000000026fc2b4c76d0dc16be1c31d4c1dc53bf9b45987fc75c0000000000000000000026f2e7e90f5a767406eff87fdad7eb07ef407922ec1d000006ac3d9880d183b820ab21be370d5312f44cb42ce377bc9b8a0cef1a4c83000000000000000000000000000000000000000000000000000000000000000400000000000000000000000004068da6c83afcfa0e13ba15a6696662335d5b7500000000000000000000000004068da6c83afcfa0e13ba15a6696662335d5b7500000000000000000000000021be370d5312f44cb42ce377bc9b8a0cef1a4c8300000000000000000000000021be370d5312f44cb42ce377bc9b8a0cef1a4c83",
        "nonce": "0x1c1",
        "to": "0xe836817fca0562b0e4cf6b819a12a1b1c8e216a4",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x0",
        "v": "0x217",
        "r": "0x448533528d7145bef92999087af6f6666ceb7ce3f29d234a42ff20aa5ce48ba4",
        "s": "0x2a16e92fc107b765c1f22c0d88eb33572d58c90eceab6ed909a46d5d43efccd7"
    }
}
```
{% endcode %}
