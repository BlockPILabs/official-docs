---
description: Returns the information about a transaction requested by transaction hash.
---

# eth\_getTransactionByHash

#### hekla**Parameters:**

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
curl https://taiko-hekla.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xc5bea677963e5f4600e9ebd7d8237239a5f09a0aa5057fd7bc323c0a3defc446"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x66fd5b48d3a9d3a3a4476bd2572750d0335e2623f19b1aaa4df1d45fa2a34d2b",
        "blockNumber": "0x17af818",
        "from": "0x2737840364fba5642f96ea530f21a43e69a70f59",
        "gas": "0x5208",
        "gasPrice": "0x66720b300",
        "hash": "0xc5bea677963e5f4600e9ebd7d8237239a5f09a0aa5057fd7bc323c0a3defc446",
        "input": "0x",
        "nonce": "0x11b",
        "to": "0xe4119e8ca4ed74fc37871a475cf53eec66da15c2",
        "transactionIndex": "0x0",
        "value": "0x29a2241af62c0000",
        "type": "0x0",
        "chainId": "0xa86a",
        "v": "0x150f7",
        "r": "0x2ebdca67ee46402d7ac6ff047895ea9f3379f3e52532d73fbb33054b946c4122",
        "s": "0x66a11cbe82d0f66cbf8bb678bac3a5a199636d971d24fb14b3604a2392d545e5"
    }
}
```
{% endcode %}
