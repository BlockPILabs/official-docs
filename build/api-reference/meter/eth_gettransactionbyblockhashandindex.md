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
curl https://meter.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x0239a5a4ef5519facf58e8dff807705840bc806bd90e9861e90e75f81b801f74", 0],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "hash": "0x9547a073d5bfc8bf7850103d9bbf466312e761b49f84f548904badabbff81d16",
        "nonce": "0xfe87eec1",
        "blockHash": "0x0239a5a4ef5519facf58e8dff807705840bc806bd90e9861e90e75f81b801f74",
        "blockNumber": "0x239a5a4",
        "transactionIndex": "0x0",
        "from": "0x8dba92fca6afaf48fbabb12337250f7bae672b98",
        "to": "0x1adcef5c780d8895ac77e6ee9239b4b3ecb76da2",
        "value": "0x0",
        "gas": "0xc719",
        "gasPrice": "0x1",
        "input": "0x095ea7b3000000000000000000000000479d176c2c9968a3d47a42b99915ddf5bfa9ff560000000000000000000000000000000000000000000000000000000842458b63",
        "r": "0x581794787130615fbb22bbae3abc273a09bd1fb44ff6efeb36534f096f93351f",
        "s": "0x50620e136f2d802f409929b9beeba2a772814099b8f2a4e12fb50e78150422d5",
        "v": "0x1"
    }
}
```
{% endcode %}
