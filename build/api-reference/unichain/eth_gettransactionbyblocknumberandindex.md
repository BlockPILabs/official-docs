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
curl https://unichain.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xda4a0cb54856feda8a75a68d8b306a904c510e061c5e3ad8944af4169fbfb1a1",
        "blockNumber": "0x3e7fa02",
        "from": "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0001",
        "gas": "0xf4240",
        "gasPrice": "0x0",
        "hash": "0x111b6cd055a4d911915b60e97ae3830251cdfe6b3d311748946c6b87ac59e4c9",
        "input": "0x015d8eb90000000000000000000000000000000000000000000000000000000001339963000000000000000000000000000000000000000000000000000000006678e5d30000000000000000000000000000000000000000000000000000000090e8647a6df86e42e239bafe7d8083a763300385bfcbb1e32863195ac8826a9bf438e85000000000000000000000000000000000000000000000000000000000000000020000000000000000000000002f40d796917ffb642bd2e2bdd2c762a5e40fd74900000000000000000000000000000000000000000000000000000000000000bc0000000000000000000000000000000000000000000000000000000000002710",
        "nonce": "0x429117",
        "to": "0x4200000000000000000000000000000000000015",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x7e",
        "v": "0x0",
        "r": "0x0",
        "s": "0x0",
        "sourceHash": "0xac201f68d62639ca9940065da8f898e44ddb62b12f7a0cd5fee388331f102b0c",
        "mint": "0x0",
        "ethValue": "0x0"
    }
}
```
{% endcode %}
