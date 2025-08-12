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
curl https://flow-evm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xe0ae8362820fab73abd9f7aec578308f36d2c81ac71f434d864b43f13c5e227b",
        "blockNumber": "0x1aef754",
        "from": "0x4404ba1717eab3f3dec6565c51b87e86d14e064c",
        "gas": "0x154f7d",
        "gasPrice": "0x2018a9b298",
        "feeCurrency": null,
        "gatewayFeeRecipient": null,
        "gatewayFee": "0x0",
        "hash": "0x09e11634ed9e7762a8706419b60e74a4f05aae7424cf1122fe3f4be4f392103a",
        "input": "0x000000300000000000054f9347e644b3dda0471ece3750da237f93b8e339c536989b8978a438016cde5f5a192fbf3fd84df983aa6dc30dbd9f8fac1f00628cb3a5a206956423d158009612813b64b19dab0b000000000000000000000000000000000000000002",
        "nonce": "0x2fc3f",
        "to": "0xe2ef41a93dab1878310e81617da47995f6ec01fe",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x0",
        "v": "0x149fb",
        "r": "0xef5be040cb5d3146e12df8558cf80d9090a4b14988795a59104d78a3aa1059cc",
        "s": "0x38b5e3b98451dd3dc94f79b6e3fbbd8052243b450605638f0c3c78dc75706b85",
        "ethCompatible": true
    }
}
```
{% endcode %}
