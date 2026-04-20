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
```python
// Request
curl https://arc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x9ac2d3d881982c48172357e7701e56c313018bda15f46806a37e38dd8efb9503"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "type": "0x0",
        "chainId": "0x4cef52",
        "nonce": "0x170d",
        "gasPrice": "0x60dcc5a20",
        "gas": "0x186a0",
        "to": "0x3600000000000000000000000000000000000000",
        "value": "0x0",
        "input": "0xa9059cbb0000000000000000000000006c9b2bba5f6481493c3019bff2a7576e83746d6d0000000000000000000000000000000000000000000000000000000000018615",
        "r": "0x85ac005aad44b044df575e289bd650177b90c8756f3263f6bef478770e979bfa",
        "s": "0x737b86dd320b71504ebb56dd19244b54f131d2905fa0ed9b859cfc75cd2e20b0",
        "v": "0x99dec7",
        "hash": "0x9ac2d3d881982c48172357e7701e56c313018bda15f46806a37e38dd8efb9503",
        "blockHash": "0x18668d413f7060e9d2e4abf76342b46aff0711fef2719551ddbd10ff69f17358",
        "blockNumber": "0x24517e2",
        "transactionIndex": "0x0",
        "from": "0xbe2a011607ca89513de0cf25b8a534cd5c295318"
    }
}
```
{% endcode %}
