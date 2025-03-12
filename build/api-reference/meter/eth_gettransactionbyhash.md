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
curl https://meter.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xa5007c001f18b75b3ff0beb5b394734fcdfcf54fac808f4fefc50fb9aa770ff7"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "hash": "0xa5007c001f18b75b3ff0beb5b394734fcdfcf54fac808f4fefc50fb9aa770ff7",
        "nonce": "0xea042d7c",
        "blockHash": "0x0239756b04ab15911279a75860d93f3867f1de3086b840175351d4d10e2bb50d",
        "blockNumber": "0x239756b",
        "transactionIndex": "0x0",
        "from": "0xb9fe947d6e3c03b190df441da142127878af1343",
        "to": "0x2c3b31f752bd3bbefec6b1f0e82c47575e42db93",
        "value": "0x0",
        "gas": "0x1da61",
        "gasPrice": "0x1",
        "input": "0x23b872dd000000000000000000000000b9fe947d6e3c03b190df441da142127878af13430000000000000000000000009b2461f63718cb895a3a29a4eee4f4fcb15dea88c000000000000000000002000000006458bb4c010000000500000000000001ef",
        "r": "0xf37cf1be5dfab24436cdf76cd4694dc9954070a4dee7b35a3193c165b17fb850",
        "s": "0x6af2e5776347949b4b4a5d803a7830f201153b488cace8271df68568dcae08fe",
        "v": "0xc8"
    },
    "id": 1
}
```
{% endcode %}
