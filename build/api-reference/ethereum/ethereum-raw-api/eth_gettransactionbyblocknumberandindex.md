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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0xF2F8D7", "0x0"],"id":1}'

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":{
        "blockHash":"0xa8d01d6d5e70cb3bd8cd423eaa11714b89adef041141e4ca31bcdc6879543b23",
        "blockNumber":"0xf2f8d7",
        "from":"0x255ed4ae17eff35923cfde87ed6ce81c4ebf8888",
        "gas":"0x34b15",
        "gasPrice":"0x38d12211e",
        "maxPriorityFeePerGas":"0x0",
        "maxFeePerGas":"0x71a24423c",
        "hash":"0x4878fb96953eea6db8dee22787214b51fa875a2dbc9fef8984602c60f39f10b6",
        "input":"0x0311b815efb8f581194ae79006d24e0d814b7697f600000007f0fe144fa826e0703b120f15ab77b986a24c6f9262364d02f9432f1000000007e5d1a3df71d7a7",
        "nonce":"0x4a74","to":"0x38a868000000a600a300867c596d400d79970500",
        "transactionIndex":"0x0",
        "value":"0x0",
        "type":"0x2",
        "accessList":[{
            "address":"0xdac17f958d2ee523a2206206994597c13d831ec7",
            "storageKeys":["0x0000000000000000000000000000000000000000000000000000000000000000","0x3ad2db55fe5657fe773e3b7111e43f4b662a181a20e875b3b8be52dd9f0e2333","0x000000000000000000000000000000000000000000000000000000000000000a","0x0000000000000000000000000000000000000000000000000000000000000003","0x0000000000000000000000000000000000000000000000000000000000000004","0x169228ca33ea854d54aa1e506e59ec687f618a41074f5f5de937a0e9c6343e5a","0x7b4dde3b0741d562eb26de87cf5d4054b17e06762c01945d8239f651a1eb56d8"]
            },{
            "address":"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "storageKeys":["0x0cb865ff1951c90111975d77bc75fa8312f25b08bb19b908f6b9c43691ac0caf","0xc03bfebcb17457ccd303a02ee88d0023c8543130f3e1c1dcf3fe4102963b55e2","0x2dff7e872c41ba172ddc85e3a80562af43838886f636afbc7f1366a43f2112bf"]
            },{
            "address":"0x703b120f15ab77b986a24c6f9262364d02f9432f",
            "storageKeys":["0x0000000000000000000000000000000000000000000000000000000000000009","0x000000000000000000000000000000000000000000000000000000000000000a","0x000000000000000000000000000000000000000000000000000000000000000f","0x0000000000000000000000000000000000000000000000000000000000000008","0x0000000000000000000000000000000000000000000000000000000000000006","0x0000000000000000000000000000000000000000000000000000000000000007","0x000000000000000000000000000000000000000000000000000000000000000c"]
            },{
            "address":"0x11b815efb8f581194ae79006d24e0d814b7697f6",
            "storageKeys":["0x0000000000000000000000000000000000000000000000000000000000000001","0x32d80bb380a6153715a380340a591610b4f5a62ca0809dce09eefe0e7c37ea7f","0x0000000000000000000000000000000000000000000000000000000000000000","0x0000000000000000000000000000000000000000000000000000000000000004"]
            }],
        "chainId":"0x1",
        "v":"0x1",
        "r":"0x9ff409602f06003de46220e60eeaf2bbeeed7e0b5e8904955e42785dc739a8b",
        "s":"0x49c9d172837241dcee1e6fa4f09df55e9f767636a2680d423284dce835350ba"}
}
```
{% endcode %}
