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
curl https://metis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
        "blockNumber": "0x11f4880",
        "from": "0xccd77d7c2ad41115b6dd60c2b8c87ea3b1b117ff",
        "gas": "0x1e899f",
        "gasPrice": "0x53f5d100",
        "hash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
        "input": "0x52aa4c2200000000000000000000000000000000000000000002425cfa2a72b13e8863000000000000000000000000000000000000000000000000001d4ec7feed60192000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000ccd77d7c2ad41115b6dd60c2b8c87ea3b1b117ff000000000000000000000000858b562b4ffded8f05efbc2baa03836f0492508a00000000000000000000000000000000000000000000000000000000672073cf0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000fbae1eab52af0ea3d35cb12f1221ce32d377d08e00000000000000000000000075cb093e4d61d2a2e65d8e0bbb01de8d89b53481",
        "nonce": "0x1b8",
        "to": "0x14679d1da243b8c7d1a4c6d0523a2ce614ef027c",
        "transactionIndex": "0x0",
        "value": "0x0",
        "v": "0x8a3",
        "r": "0x3884b0f0328d19cee9daaca07c35918f0025736fb3fbefd76e7e5e28fa842f61",
        "s": "0x4b3c96192c5a0550778aabdfe0d04271cc208cf524989c8581ef2d1ed061186",
        "queueOrigin": "sequencer",
        "l1TxOrigin": "0x0000000000000000000000000000000000000000",
        "l1BlockNumber": "0x1417b4f",
        "l1Timestamp": "0x672057b8",
        "index": "0x11f487f",
        "queueIndex": "0x0",
        "rawTransaction": "0xf9018e8201b88453f5d100831e899f9414679d1da243b8c7d1a4c6d0523a2ce614ef027c80b9012452aa4c2200000000000000000000000000000000000000000002425cfa2a72b13e8863000000000000000000000000000000000000000000000000001d4ec7feed60192000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000ccd77d7c2ad41115b6dd60c2b8c87ea3b1b117ff000000000000000000000000858b562b4ffded8f05efbc2baa03836f0492508a00000000000000000000000000000000000000000000000000000000672073cf0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000fbae1eab52af0ea3d35cb12f1221ce32d377d08e00000000000000000000000075cb093e4d61d2a2e65d8e0bbb01de8d89b534818208a3a03884b0f0328d19cee9daaca07c35918f0025736fb3fbefd76e7e5e28fa842f61a004b3c96192c5a0550778aabdfe0d04271cc208cf524989c8581ef2d1ed061186",
        "seqR": "0x72ea3eddb963950dec6f2a4c16dafb38687df19dd5c530f7a35f8f0e611740bf",
        "seqS": "0x3616ff0dbccc5e0413e82ce660a4c20339d627d23df411ee7f16257a44b54a56",
        "seqV": "0x1"
    }
}
```
{% endcode %}
