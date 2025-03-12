---
description: Returns useful L2-specific information about the current node.
---

# rollup\_getInfo

#### **Parameters:**

None

#### **Returns:**

**Object:**

* **mode: STRING** - `"sequencer"` or `"verifier"` depending on the node's mode of operation
* **syncing: BOOLEAN** - `true` if the node is currently syncing, `false` otherwise
* **ethContext: OBJECT**
  * **blockNumber: QUANTITY** - Block number of the latest known L1 block
  * **timestamp: QUANTITY** - Timestamp of the latest known L1 block
* **rollupContext: OBJECT**
  * **queueIndex: QUANTITY** - Index within the CTC of the last L1 to L2 message ingested
  * **index: QUANTITY** - Index of the last L2 tx processed
  * **verifiedIndex: QUANTITY** - Index of the last tx that was ingested from a batch that was posted to L1

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"rollup_getInfo","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "mode": "verifier",
        "syncing": false,
        "ethContext": {
            "blockNumber": 16131692,
            "timestamp": 1670402841
        },
        "rollupContext": {
            "index": 46308439,
            "queueIndex": 227091,
            "verifiedIndex": 0
        }
    }
}
```
{% endcode %}
