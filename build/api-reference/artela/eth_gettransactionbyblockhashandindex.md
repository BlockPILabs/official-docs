---
description: Returns the information about a transaction requested by Block hash and index.
---

# eth\_getTransactionByBlockHashAndIndex

#### **Parameters:**

**DATA , 32 Bytes** - Hash of a block.

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
curl https://artela-testnet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0xf0aa3d4d32ae75a1f3433f22a703c4be762475eb2b1822ec71573ff360bb5799", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xf0aa3d4d32ae75a1f3433f22a703c4be762475eb2b1822ec71573ff360bb5799",
        "blockNumber": "0x709587",
        "from": "0x1c3b7c3f965863cc97b253e1aaef315309923018",
        "gas": "0x55e8",
        "gasPrice": "0x59682f07",
        "maxFeePerGas": "0x59682f08",
        "maxPriorityFeePerGas": "0x59682f00",
        "hash": "0x18ae964b3ee99d0beaa22ab7549e817aba57281d461a2f615ec541645db3a95c",
        "input": "0x646174613a2c7b2270223a226172742d3230222c226f70223a226d696e74222c227469636b223a2277617665312e32222c22616d74223a2231303030227d",
        "nonce": "0x1e066",
        "to": "0x1c3b7c3f965863cc97b253e1aaef315309923018",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x2",
        "accessList": [],
        "chainId": "0x2e2e",
        "v": "0x0",
        "r": "0x54c8cfc85c8882746784d7086d5da6d59d07ff6a3e905b2e8cead88c83464c7",
        "s": "0x473cb8175936ea953d37e1895cd680e10c273a2f8d3c2b150b38bb0d7c0e6d68"
    }
}
```
{% endcode %}
