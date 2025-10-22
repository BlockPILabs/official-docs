---
description: >-
  Polling method for a filter, which returns an array of logs which occurred
  since last poll.
---

# kaia\_getFilterChanges

#### **Parameters**

| Name     | Type   | Description                                             |
| -------- | ------ | ------------------------------------------------------- |
| QUANTITY | string | <p>The filter id (<em>e.g.</em>, "0x16" // 22).<br></p> |

#### **Return Value**

`Array` - Array of log objects, or an empty array if nothing has changed since last poll.

| Name             | Type          | Description                                                                                                                                                                                                                                  |
| ---------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| removed          | TAG           | `true` when the log was removed, due to a chain reorganization. `false` if it is a valid log.                                                                                                                                                |
| logIndex         | QUANTITY      | Integer of the log index position in the block. `null` when it is a pending log.                                                                                                                                                             |
| transactionIndex | QUANTITY      | Integer of the transactions index position log was created from. `null` when pending.                                                                                                                                                        |
| transactionHash  | 32-byte DATA  | Hash of the transactions this log was created from. `null` when pending.                                                                                                                                                                     |
| blockHash        | 32-byte DATA  | Hash of the block where this log was in. `null` when pending.                                                                                                                                                                                |
| blockNumber      | QUANTITY      | The block number where this log was in. `null` when pending.Address from which this log originated.                                                                                                                                          |
| address          | 20-byte DATA  | Address from which this log originated.                                                                                                                                                                                                      |
| data             | DATA          | Contains the non-indexed arguments of the log.                                                                                                                                                                                               |
| topics           | Array of DATA | Array of 0 to 4 32-byte DATA of indexed log arguments. (In Solidity: The first topic is the hash of the signature of the event (_e.g._, `Deposit(address,bytes32,uint256)`), except you declared the event with the `anonymous` specifier.). |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_getFilterChanges","params":["0x16"],"id":73}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
    "id":1,
    "jsonrpc":"2.0",
    "result": [{
    "logIndex": "0x1", // 1
    "blockNumber":"0x1b4", // 436
    "blockHash": "0x8216c5785ac562ff41e2dcfdf5785ac562ff41e2dcfdf829c5a142f1fccd7d",
    "transactionHash":  "0xdf829c5a142f1fccd7d8216c5785ac562ff41e2dcfdf5785ac562ff41e2dcf",
    "transactionIndex": "0x0", // 0
    "address": "0x16c5785ac562ff41e2dcfdf829c5a142f1fccd7d",
    "data":"0x0000000000000000000000000000000000000000000000000000000000000000",
    "topics": ["0x59ebeb90bc63057b6515673c3ecf9438e5058bca0f92585014eced636878c9a5"]
    },{
        ...
    }]
}
```
{% endcode %}
