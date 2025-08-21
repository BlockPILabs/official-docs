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
curl https://hemi.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"topics": ["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b"]}],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": [ ]
}
```
{% endcode %}
