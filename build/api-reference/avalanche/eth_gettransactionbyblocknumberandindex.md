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
curl https://avalanche.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0xF2F8D7", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x34a37fba236980dc9f0194fef13aef73150c2b8c0dc7008d7619f304a415851e",
        "blockNumber": "0xf2f8d7",
        "from": "0xbfb5f9ea7199cdf1dff111e02ca124eaa3ae1b08",
        "gas": "0xf4240",
        "gasPrice": "0x8d8f9fc00",
        "hash": "0xee078aa1c5c8d8dff9f7b2d9bd0b61f90625e119f3a2418b6248db11e301e8af",
        "input": "0xc43ed2c800000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000040000000000000000000000000b31f66aa3c1e785363f0875a1b74e27b85fd66c70000000000000000000000000000000000000000000000000000000001176229",
        "nonce": "0x1e1b",
        "to": "0x8e955737e2acb12d8b0f2d765c7d9ea125547b01",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x0",
        "chainId": "0xa86a",
        "v": "0x150f8",
        "r": "0xff63afb36e8e2ad4831f2df95ea68e5f50eb9329de87f21f90308a8e39a336c2",
        "s": "0x73ee32cd77d96fc909d34e60c5ffa6b75a1fd19142582cee912a717baf0cb4b1"
    }
}
```
{% endcode %}
