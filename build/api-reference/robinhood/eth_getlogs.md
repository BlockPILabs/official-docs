# eth\_getlogs

#### **Parameters:**

**Object** - The filter options:

* **fromBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **toBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **address: DATA|Array, 20 Bytes** - (optional) Contract address or a list of addresses from which logs should originate.
* **topics: Array of DATA** - (optional) Array of 32 Bytes DATA topics. Topics are order-dependent. Each topic can also be an array of DATA with "or" options.
* **blockhash: DATA, 32 Bytes** - (optional, future) With the addition of EIP-234, blockHash will be a new filter option which restricts the logs returned to the single block with the 32-byte hash blockHash.

{% hint style="info" %}
The block range of eth\_getLogs is limited to **1024** for public endpoints and **5000** for private endpoints. Requests with blocks over this range will get an error.
{% endhint %}

#### **Returns:**

**Array** - Array of log objects.

* **removed: TAG** - true when the log was removed, due to a chain reorganization.
* **logIndex: QUANTITY** - integer of the log index position in the block.
* **transactionIndex: QUANTITY** - integer of the transactions index position log was created from.
* **transactionHash: DATA, 32 Bytes** - hash of the transactions this log was created from.
* **blockHash: DATA, 32 Bytes** - hash of the block where this log was in.
* **blockNumber: QUANTITY** - the block number where this log was in.
* **blockTimestamp: QUANTITY** - the block timestamp.
* **address: DATA, 20 Bytes** - address from which this log originated.
* **data: DATA** - contains one or more 32 Bytes non-indexed arguments of the log.
* **topics: Array of DATA** - Array of 0 to 4 32 Bytes DATA of indexed log arguments.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"fromBlock":"0x90a6f0","toBlock":"0x90a6f2"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "address": "0xa870f8c7cae9705194a141b0c2964b6c79ee3742",
      "topics": [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x00000000000000000000000098117495f7685703bf97ee95a31fcd212993936f",
        "0x000000000000000000000000cfe030a420e694351fd79ba6486f99f11b1296e2"
      ],
      "data": "0x0000000000000000000000000000000000000000000000005fc1b97136320000",
      "blockNumber": "0x90a6f0",
      "transactionHash": "0x63af9c5fdde337df0f35b0985fd0999fe1631fc54cdc855c1c7e1dab4dc82c54",
      "transactionIndex": "0x1",
      "blockHash": "0x40cf0fbc2de92ccccdba3725b220a0be92429a2d02a5448e90d0f8f9750ce865",
      "blockTimestamp": "0x6a561826",
      "logIndex": "0x0",
      "removed": false
    },
    "..."
  ]
}
```
{% endcode %}
