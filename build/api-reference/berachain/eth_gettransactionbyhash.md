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
curl https://berachain-bartio.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xdbb44c46e7f0c37a7949ca8b175f89837f3a1e9516f467cb713eb388b9d87719"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xf4f9b4afce90777939f7abfc6477248c7a1fc54b10ff662b0b2657420332e3e3",
        "blockNumber": "0x35c74",
        "from": "0xdcd40f0d719d543d68c5a29c57becb1a3324fcce",
        "gas": "0x5208",
        "gasPrice": "0x14b71d692",
        "hash": "0xdbb44c46e7f0c37a7949ca8b175f89837f3a1e9516f467cb713eb388b9d87719",
        "input": "0x",
        "nonce": "0x0",
        "to": "0xb00b5c688cc8f68ca0aeeae6a0ab0712d7eb2d67",
        "transactionIndex": "0x1",
        "value": "0x38d7ea4c68000",
        "type": "0x1",
        "accessList": [],
        "chainId": "0x138d4",
        "v": "0x0",
        "r": "0xbbaed58824acd2098a4d7fd592bdad8806120a4b86933165cd9ae3695e8705ea",
        "s": "0x4e47ca89037a86dd2cca37eabfa6083c82aaf18bb7dc01c1d6512c116e60af92",
        "yParity": "0x0"
    }
}
```
{% endcode %}
