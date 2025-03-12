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
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xf0d0b41d8ad67df9b4b2dcb22dcf407673d7dc64985168f001c630dd56c347e2",
        "blockNumber": "0x16c94d6",
        "from": "0xf598452bfc73b34bf74cef41327cf0d9f76b4b62",
        "gas": "0x5208",
        "gasPrice": "0x12a05f200",
        "hash": "0x2e1fbc191c7e87a345a9e8693005280afc5cb60624ca10e08c4cdededf2c5d3b",
        "input": "0x",
        "nonce": "0x37ce6",
        "to": "0x207dfa006ed8fe79e2eef5b6e1299a2510f3e067",
        "transactionIndex": "0x55",
        "value": "0x7b4a85a55000",
        "type": "0x0",
        "chainId": "0x38",
        "v": "0x93",
        "r": "0xebcd671469f19b3c4297392970d5a523c50aaffdd2511e3e50c03d5b622fb85e",
        "s": "0x6460a0a7194d6fb0ac326f7071856ae5aa379ba072fce0417453665a592c7b4a"
    }
}
```
{% endcode %}
