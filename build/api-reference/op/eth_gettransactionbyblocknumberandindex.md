---
description: >-
  Returns the information about a transaction requested by Block number and
  index.
---

# eth\_getTransactionByBlockNumberAndIndex

#### **Parameters:**

**QUANTITY|TAG** - Integer block number encoded as a hexadecimal, or the string 'latest', 'earliest' or 'pending'.

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
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xdc7021b7ebbe4389f67ac030009bc7d3c490a1fc26931b74876cfde62f73808a",
        "blockNumber": "0x2b69312",
        "from": "0x9e4c4164fc0e29f3fdc9d928ecec393ddd876d9e",
        "gas": "0x2bd23",
        "gasPrice": "0xf4240",
        "hash": "0xe6a48601320c4837734a9562dd609247a3688554aa997b16c465d056edc138cf",
        "input": "0xc634d0320000000000000000000000000000000000000000000000000000000000000001",
        "nonce": "0x1d",
        "to": "0xab586a06b98df0a86dcd4e1a0294a404c6284725",
        "transactionIndex": "0x0",
        "value": "0x0",
        "v": "0x37",
        "r": "0xe267af3a53762bfc89482933f4dd112a153da49eb712d1a1c785cccbc2e3090b",
        "s": "0x24e5f8f0034b6977eac3e79e1bec6333656b0da01b49c9212c2600e7d52ed3ba",
        "queueOrigin": "sequencer",
        "l1TxOrigin": null,
        "l1BlockNumber": "0xf5eb07",
        "l1Timestamp": "0x638d82a9",
        "index": "0x2b69311",
        "queueIndex": null,
        "rawTransaction": "0xf8871d830f42408302bd2394ab586a06b98df0a86dcd4e1a0294a404c628472580a4c634d032000000000000000000000000000000000000000000000000000000000000000137a0e267af3a53762bfc89482933f4dd112a153da49eb712d1a1c785cccbc2e3090ba024e5f8f0034b6977eac3e79e1bec6333656b0da01b49c9212c2600e7d52ed3ba"
    }
}
```
{% endcode %}
