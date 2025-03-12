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
curl https://mantle.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x426920cdcd5cda439509724ed7c2aa55b8de461eb609406e94746bbbc9dddfd6"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x27f3363d84f6862ba3d5fffb6e3bd151e015b2321b2fb41bcab275b7db424aa2",
        "blockNumber": "0x3e7f974",
        "from": "0x8f7798bd8eb184da2114b74154cc302ace37e040",
        "gas": "0x3c1ccccc",
        "gasPrice": "0x1315410",
        "maxFeePerGas": "0x2628110",
        "maxPriorityFeePerGas": "0x2710",
        "hash": "0x426920cdcd5cda439509724ed7c2aa55b8de461eb609406e94746bbbc9dddfd6",
        "input": "0x729d4516000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000006678e5280000000000000000000000000000000000000000000000000000000000000001000000000000000000000000459462374a5a4768c3c1b0e1d2fabaa1917e813500000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000018fc89176f6",
        "nonce": "0xe9b8",
        "to": "0x9b63c5b7a68573bbc47336ec0247798411f561b9",
        "transactionIndex": "0x1",
        "value": "0x0",
        "type": "0x2",
        "accessList": [],
        "chainId": "0x1388",
        "v": "0x1",
        "r": "0xd746eaff648ceaf70214bcb9c5308430258eac082ae9e249253819c163140efb",
        "s": "0x45c8f0adbcda46d568a714f340478cd50f312a4a74621e9a8d8237b3a1c72a3f"
    }
}
```
{% endcode %}
