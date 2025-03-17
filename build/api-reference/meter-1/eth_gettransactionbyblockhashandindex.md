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
curl https://monad.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x33b3f51da4bb4d0753b6860c591e08890048adce5388f43cbc795c4d91eb5890", 0],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "type": "0x0",
        "chainId": "0x279f",
        "nonce": "0x565",
        "gasPrice": "0xe87547000",
        "gas": "0xd3e15",
        "to": "0x590b03d84441c1277f32784d1fbc22fe18b1eee0",
        "value": "0x0",
        "input": "0xa415bcad000000000000000000000000aeef2f6b429cb59c9b2d7bb2141ada993e8571c30000000000000000000000000000000000000000000000000bac16a563219400000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000008477a066a11fc78da4b9b90aec8f598c36637f81",
        "r": "0x2c058439ac7da8423b7a20d5af8c2f1034d1301954599a7e8c5b48352580fe74",
        "s": "0x45150cba5b99e55b3f0608277d91b54ab1cfa4aa648024d269888ac591f7c0b",
        "v": "0x4f62",
        "hash": "0x47d261f2d7993288c06fd97b5411c0ca9ea341b93fe83eb37ff77f3787bd601b",
        "blockHash": "0x33b3f51da4bb4d0753b6860c591e08890048adce5388f43cbc795c4d91eb5890",
        "blockNumber": "0x7c2de7",
        "transactionIndex": "0x0",
        "from": "0x8477a066a11fc78da4b9b90aec8f598c36637f81"
    },
    "id": 1
}
```
{% endcode %}
