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
curl https://cronos.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0x6c3a5e", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xeae7a314317c565cca1ced26f09d1cd50a8a0c31c40336e5e9244f799cd5de20",
        "blockNumber": "0x6c3a5e",
        "from": "0x9ecb46c92ae036465c43a26b7918c325a82ae92d",
        "gas": "0x32c40",
        "gasPrice": "0x45eef738940",
        "hash": "0xa84ebbd2c5ffbbf743d3ae85346d46ee183db8d5286a1936e26a70b2ea12aab5",
        "input": "0xe2bbb15800000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x161a",
        "to": "0xb676b77ba1401d8b7e6e9d69081edd203f3fc1cc",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x0",
        "v": "0x55",
        "r": "0x84815dd661ae9a47803b9ace5b0bfe52823a9ad727d9386d128f6cdd95a1ad27",
        "s": "0x56c348b1d6211926711316f8e8acd4a2e800908819c5ac7c38495feb1bd61199"
    }
}
```
{% endcode %}
