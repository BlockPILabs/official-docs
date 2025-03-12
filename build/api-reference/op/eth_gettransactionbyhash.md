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
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
        "blockNumber": "0x2b65895",
        "hash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
        "from": "0x17281460228691b044e080a5f5257dce8e47f79c",
        "gas": "0x258b3",
        "gasPrice": "0xf4240",
        "input": "0x31cd52b0000000000000000000000000000000000000000000000001301780fb3e29e194000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000638d7528000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000079fc2b78439e41620000000000000000000000000000000000000000000000000000000000c89cc0",
        "nonce": "0x21",
        "r": "0xf947884ee397d03d3bfcd6cca36523c43e4bb552e081e6f6f29844f8b8a24e2e",
        "s": "0x76135cf75bc92c314a04bc7f4441dc201fe430851bc16292fe0d145e76057d22",
        "to": "0xf44938b0125a6662f9536281ad2cd6c499f22004",
        "transactionIndex": "0x0",
        "v": "0x37",
        "value": "0x0",
        "l1BlockNumber": "0xf5e9b6",
        "l1Timestamp": "0x638d72dd",
        "index": "0x2b65894",
        "queueOrigin": "sequencer",
        "rawTransaction": "0xf9012821830f4240830258b394f44938b0125a6662f9536281ad2cd6c499f2200480b8c431cd52b0000000000000000000000000000000000000000000000001301780fb3e29e194000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000638d7528000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000079fc2b78439e41620000000000000000000000000000000000000000000000000000000000c89cc037a0f947884ee397d03d3bfcd6cca36523c43e4bb552e081e6f6f29844f8b8a24e2ea076135cf75bc92c314a04bc7f4441dc201fe430851bc16292fe0d145e76057d22"
    }
}
```
{% endcode %}
