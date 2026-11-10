# eth\_feehistory

#### **Parameters:**

**QUANTITY** - Number of blocks in the requested range.

**QUANTITY|TAG** - Highest block number of the requested range, or `"latest"`.

**Array of QUANTITY** - (optional) Monotonically increasing list of percentile values to sample from each block's effective priority fees.

#### **Returns:**

**Object** - Fee history object:

* **oldestBlock: QUANTITY** - Lowest block number in the returned range.
* **baseFeePerGas: Array of QUANTITY** - Base fee per gas of each block in the range, plus the next block.
* **gasUsedRatio: Array of NUMBER** - Ratio of gas used to gas limit for each block.
* **reward: Array of Array of QUANTITY** - Priority fee per gas at each requested percentile, per block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_feeHistory","params":["0x4","latest",[25,50,75]],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "oldestBlock": "0x37a2a2",
    "reward": [
      [
        "0x0",
        "0x0",
        "0x0"
      ],
      [
        "0x0",
        "0x0",
        "0x0"
      ],
      "..."
    ],
    "baseFeePerGas": [
      "0x1dd81360",
      "0x1ddef130",
      "..."
    ],
    "gasUsedRatio": [
      1,
      1,
      "..."
    ]
  }
}
```
{% endcode %}
