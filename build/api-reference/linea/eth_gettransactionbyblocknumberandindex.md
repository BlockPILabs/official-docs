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
curl https://linea.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x4d76e4447702a7dfbccb4a9e3be640b00078290ae1a84cce58f8589b1f7ae989",
        "blockNumber": "0x24d37",
        "from": "0x45a318273749d6eb00f5f6ca3bc7cd3de26d642a",
        "gas": "0x6270",
        "gasPrice": "0x237a9ccfa",
        "maxFeePerGas": "0x2a9322923",
        "maxPriorityFeePerGas": "0x237a9ccf3",
        "hash": "0x17db0f3d77434c21e76a405e0d3a329ba0a9eadf6a767c6dd40f8149eb30651e",
        "input": "0x",
        "nonce": "0x74e7",
        "to": "0x124fb955862709e30740028cb86c477221842b14",
        "transactionIndex": "0x0",
        "value": "0x470de4df820007",
        "type": "0x2",
        "accessList": [],
        "chainId": "0xe708",
        "v": "0x1",
        "r": "0x5258ce88c9dd9ca3346c0577bc59838cd85de61e112b12c46aaf525a0af1b1da",
        "s": "0x6c8c928040c9fba1877f058125dd9a79e763c5b1be1e3240683997a75b5da5f2"
    }
}
```
{% endcode %}
