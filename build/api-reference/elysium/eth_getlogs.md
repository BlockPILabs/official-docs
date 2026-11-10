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

{% hint style="info" %}
The block range of eth\_getLogs is limited to **1024** for public endpoints and **5000** for private endpoints. Requests with blocks over this range will get an error.
{% endhint %}

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"fromBlock":"0x37a200","toBlock":"0x37a200"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "address": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
      "topics": [
        "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
        "0x000000000000000000000000148ddcefd47234b60d4fe0463f7497ef7a71a27b",
        "0x000000000000000000000000ca0d2b3047e547fd256c325db04634fa923aab52"
      ],
      "data": "0x000000000000000000000000000000000000000000000d51097a8a84d0836dc5",
      "blockNumber": "0x37a200",
      "transactionHash": "0xc6ed0a1582d665eca7f4d61f87d9ec72c58b6643ec864af2b6ed8dd665356a03",
      "transactionIndex": "0x1",
      "blockHash": "0xd0eec69c7e7de05ba0e5202d1c50dffe42d897396637d35ee169bbb9fa55cf5f",
      "blockTimestamp": "0x6af2738d",
      "logIndex": "0x0",
      "removed": false
    },
    {
      "address": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
      "topics": [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x000000000000000000000000148ddcefd47234b60d4fe0463f7497ef7a71a27b",
        "0x000000000000000000000000e2e105d3f7209a9da11f83ccf3e7398a753823f1"
      ],
      "data": "0x000000000000000000000000000000000000000000000d51097a8a84d0836dc5",
      "blockNumber": "0x37a200",
      "transactionHash": "0xa9b1e87782454a7b64d55c0bd8883febfbcab78e6dfcdf5f517e43fa6a1f0870",
      "transactionIndex": "0x2",
      "blockHash": "0xd0eec69c7e7de05ba0e5202d1c50dffe42d897396637d35ee169bbb9fa55cf5f",
      "blockTimestamp": "0x6af2738d",
      "logIndex": "0x1",
      "removed": false
    },
    "..."
  ]
}
```
{% endcode %}
