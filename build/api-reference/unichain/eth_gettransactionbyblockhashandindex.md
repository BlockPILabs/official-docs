---
description: Returns the information about a transaction requested by Block hash and index.
---

# eth\_getTransactionByBlockHashAndIndex

#### **Parameters:**

**DATA , 32 Bytes** - Hash of a block.

**QUANTITY** - A decimal of the integer representing the position in the block.

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
curl https://unichain.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0xaf98e4c6aa97905a4b6d6d977d81d1d1629d72545913346ab3c6e1197e556df7", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xaf98e4c6aa97905a4b6d6d977d81d1d1629d72545913346ab3c6e1197e556df7",
        "blockNumber": "0x2abb5e",
        "from": "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0001",
        "gas": "0xf4240",
        "gasPrice": "0x0",
        "hash": "0x1b43eaf62ae3398df8bee31d9b3146fc11626c0e52e2bd0ff2ff1b97866dc705",
        "input": "0x440a5e20000007d0000dbba000000000000000000000000067186878000000000069b0fa0000000000000000000000000000000000000000000000000000000010504b2500000000000000000000000000000000000000000000000000000000000001344f71a3e2c8ed9540d5e9da7ad1369b954b5a7b27a53078f0bf1274048b15dce20000000000000000000000004ab3387810ef500bfe05a49dc53a44c222cbab3e",
        "nonce": "0x2abb5d",
        "to": "0x4200000000000000000000000000000000000015",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x7e",
        "v": "0x0",
        "r": "0x0",
        "s": "0x0",
        "sourceHash": "0xb40d5aa51000b39161b803aa1ace58125ec2b22bbdb0e167d5dfc5bc00ff9d1c",
        "mint": "0x0",
        "depositReceiptVersion": "0x1"
    }
}
```
{% endcode %}
