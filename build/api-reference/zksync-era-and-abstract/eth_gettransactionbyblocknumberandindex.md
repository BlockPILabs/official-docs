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
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0x5a4", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x3d6dfa99359975a291df6a0b04629ed578143d652c7c5cc903830ecd47f77c55",
        "blockNumber": "0x5a4",
        "chainId": "0x118",
        "from": "0xe772de302f2a3c2bee3e625a261397b56ad1d9a2",
        "gas": "0x989680",
        "gasPrice": "0x0",
        "hash": "0x71bd57b9687bbb7f08f3445aae186d9e26e64808e8b96eff9796d17366208137",
        "input": "0x",
        "l1BatchNumber": "0xa1",
        "l1BatchTxIndex": "0x4",
        "maxFeePerGas": "0x0",
        "maxPriorityFeePerGas": "0x0",
        "nonce": "0x0",
        "to": "0xe772de302f2a3c2bee3e625a261397b56ad1d9a2",
        "transactionIndex": "0x0",
        "type": "0xff",
        "value": "0x6f05b59d3b20000"
    }
}
```
{% endcode %}
