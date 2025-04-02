---
description: >-
  Returns a collection of historical gas information from which you can decide
  what to submit as your maxFeePerGas and/or maxPriorityFeePerGas.
---

# eth\_feeHistory

#### **Parameters:**

**Blockcount**- Number of blocks in the requested range. Between 1 and 1024 blocks can be requested in a single query. Less than requested may be returned if not all blocks are available.

**Newestblock** - Highest number block of the requested range.

**Rewardpercentiles** - (optional) A monotonically increasing list of percentile values to sample from each block's effective priority fees per gas in ascending order, weighted by gas used.

#### **Returns:**

**Object**

* **oldestBlock**- Lowest number block of the returned range.
* **baseFeePerGas** - An array of block base fees per gas. This includes the next block after the newest of the returned range, because this value can be derived from the newest block. Zeroes are returned for pre-EIP-1559 blocks.
* **gasUsedRatio** - An array of block gas used ratios. These are calculated as the ratio of gasUsed and gasLimit.
* **reward** - (Optional) An array of effective priority fee per gas data points from a single block. All zeroes are returned if the block is empty.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"eth_feeHistory","params":[4,"latest",[25,75]],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "oldestBlock": "0x311f0d",
        "reward": [
            [
                "0x0",
                "0x0"
            ],
            [
                "0x0",
                "0x0"
            ],
            [
                "0x0",
                "0x0"
            ],
            [
                "0x0",
                "0x0"
            ]
        ],
        "baseFeePerGas": [
            "0x989680",
            "0x989680",
            "0x989680",
            "0x989680",
            "0x989680"
        ],
        "gasUsedRatio": [
            1,
            1,
            0.01047642857142857,
            0.02095285714285714
        ]
    }
}
```
{% endcode %}
