---
description: >-
  Polling method for a filter, which returns an array of logs that occurred
  since the last poll.
---

# eth\_getFilterChanges

#### **Parameters:**

**QUANTITY** - the filter id.

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
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params":["0xfbde6160d6641f29f0f3d3bb94ac6059"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": []
}
```
{% endcode %}
