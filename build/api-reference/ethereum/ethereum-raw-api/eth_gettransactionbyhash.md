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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe"],"id":1}'

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":{
        "blockHash":"0x9ed304f0736ba4acaa45a33a31ae15e81ac4e8a4eaaec8cfd5b080d46fa1acc9",
        "blockNumber":"0xf2f8d9",
        "from":"0xdafea492d9c6733ae3d56b7ed1adb60692c98bc5",
        "gas":"0x5208",
        "gasPrice":"0x40cbb6713",
        "maxPriorityFeePerGas":"0x0",
        "maxFeePerGas":"0x40cbb6713",
        "hash":"0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa",
        "input":"0x",
        "nonce":"0x14661",
        "to":"0x4675c7e5baafbffbca748158becba61ef3b0a263",
        "transactionIndex":"0x81","value":"0x95315d765ced2f",
        "type":"0x2",
        "accessList":[],
        "chainId":"0x1",
        "v":"0x1",
        "r":"0x81eb26f6ab4ffcff51997504e5f23e67f2a74f377e6335e07b30f2bc4cc600bd",
        "s":"0x633541a2e123108aed34c6bf831fa1f2f052a2529868d2737443afdc8819deac"
        }
}
```
{% endcode %}
