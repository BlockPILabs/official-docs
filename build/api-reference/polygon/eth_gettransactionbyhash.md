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
curl https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x62630cbece5d0b6791150760c1a36196bcb36f5393fe93603b7b45d818b16688",
        "blockNumber": "0x209482d",
        "from": "0x30ccf7338f608f68d3d20ab878a1be5f902047df",
        "gas": "0x11b68",
        "gasPrice": "0x6fc23ac0f",
        "maxFeePerGas": "0x6fc23ac13",
        "maxPriorityFeePerGas": "0x6fc23ac00",
        "hash": "0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe",
        "input": "0xbfbf0b4b0000000000000000000000000000000000000000000000000000000000011f8c000000000000000000000000d1feccf6881970105dfb2b654054174007f0e07e000000000000000000000000000000000000000000000000000000000000001cf19f53b2ee5ccd55bbd9d441f25e817842cd849697a7ff682b1ad28f7f7ac3e868543029b6862326448ef216eee4cc805f1985c7afcb1236098289eb331f5c49000000000000000000000000000000000000000000000000000000006343e7ce",
        "nonce": "0x19",
        "to": "0xdb46d1dc155634fbc732f92e853b10b288ad5a1d",
        "transactionIndex": "0x47",
        "value": "0x0",
        "type": "0x2",
        "accessList": [],
        "chainId": "0x89",
        "v": "0x1",
        "r": "0xa8898b885153396f0b8fa76c39bc66926b121c1c9495fdfa49e8b7e09df06c31",
        "s": "0x7d6ecb53d3e53ba4038ec865bfc160451fb96c9242cac96fb77b49e9f41c579a"
    }
}
```
{% endcode %}
