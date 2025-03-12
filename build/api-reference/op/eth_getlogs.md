---
description: Returns an array of all logs matching a given filter object.
---

# eth\_getLogs

#### **Parameters:**

**Object** - The filter options:

* **fromBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **toBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **address: DATA|Array, 20 Bytes** - (optional) Contract address or a list of addresses from which logs should originate.
* **topics: Array of DATA** - (optional) Array of 32 Bytes DATA topics. Topics are order-dependent. Each topic can also be an array of DATA with “or” options.
* **blockhash: DATA, 32 Bytes** - (optional, future) With the addition of EIP-234, blockHash will be a new filter option which restricts the logs returned to the single block with the 32-byte hash blockHash. Using blockHash is equivalent to fromBlock = toBlock = the block number with hash blockHash. If blockHash is present in the filter criteria, then neither fromBlock nor toBlock is allowed.

{% hint style="info" %}
The block range of eth\_getLogs is limited to 1024 for public endpoints and 5000 for private endpoints. Requests with blocks over this range will get an error.
{% endhint %}

#### **Returns:**

**Array** - Array of log objects, or an empty array if nothing has changed since last poll.

* For filters created with eth\_newBlockFilter the return are block hashes (DATA, 32 Bytes), e.g. \["0x3454645634534..."].
* For filters created with eth\_newFilter logs are objects with the following params:
  * **removed: TAG** - true when the log was removed, due to a chain reorganization. false if its a valid log.
  * **logIndex: QUANTITY** - integer of the log index position in the block. null when its pending log.
  * **transactionIndex: QUANTITY** - integer of the transactions index position log was created from. null when its pending log.
  * **transactionHash: DATA, 32 Bytes** - hash of the transactions this log was created from. null when its pending log.
  * **blockHash: DATA, 32 Bytes** - hash of the block where this log was in. null when its pending log.
  * **blockNumber: QUANTITY** - the block number where this log was in. null when its pending log.
  * **address: DATA, 20 Bytes** - address from which this log originated.
  * **data: DATA** - contains one or more 32 Bytes non-indexed arguments of the log.
  * **topics: Array of DATA** - Array of 0 to 4 32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"fromBlock": "latest"}],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": [
        {
            "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
            "topics": [
                "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "0x000000000000000000000000af92ae61f2deedd11bcad3c1a7625ded828774f5",
                "0x000000000000000000000000d5a8f233cbddb40368d55c3320644fb36e597002"
            ],
            "data": "0x0000000000000000000000000000000000000000000000000000000001d905c0",
            "blockNumber": "0x2b6ac9a",
            "transactionHash": "0x4544f7370d87e01e5fe1488b75f781553adca6bace818921027fa9ca2f8faaf9",
            "transactionIndex": "0x0",
            "blockHash": "0xf9fb0e63938d3dd7d9fa440c137852407d34ebdafcc3a5aef400a6c567513377",
            "logIndex": "0x0",
            "removed": false
        },
        {
            "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000af92ae61f2deedd11bcad3c1a7625ded828774f5",
                "0x000000000000000000000000d5a8f233cbddb40368d55c3320644fb36e597002"
            ],
            "data": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffe26fa3f",
            "blockNumber": "0x2b6ac9a",
            "transactionHash": "0x4544f7370d87e01e5fe1488b75f781553adca6bace818921027fa9ca2f8faaf9",
            "transactionIndex": "0x0",
            "blockHash": "0xf9fb0e63938d3dd7d9fa440c137852407d34ebdafcc3a5aef400a6c567513377",
            "logIndex": "0x1",
            "removed": false
        },
        {
            "address": "0xd5a8f233cbddb40368d55c3320644fb36e597002",
            "topics": [
                "0x1449c6dd7851abc30abf37f57715f492010519147cc2652fbc38202c18a6ee90",
                "0x000000000000000000000000af92ae61f2deedd11bcad3c1a7625ded828774f5"
            ],
            "data": "0x00000000000000000000000000000000000000000000000000000000b8c63f0000000000000000000000000000000000000000000000000000000000b226b411",
            "blockNumber": "0x2b6ac9a",
            "transactionHash": "0x4544f7370d87e01e5fe1488b75f781553adca6bace818921027fa9ca2f8faaf9",
            "transactionIndex": "0x0",
            "blockHash": "0xf9fb0e63938d3dd7d9fa440c137852407d34ebdafcc3a5aef400a6c567513377",
            "logIndex": "0x2",
            "removed": false
        }
    ]
}
```
{% endcode %}
