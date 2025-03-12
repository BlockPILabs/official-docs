---
description: Returns information about the sync status of the node
---

# eth\_syncing

#### **Parameters:**

None

#### **Returns:**

**Boolean (FALSE)** - if the node isn't syncing (which means it has fully synced)

**Object** - an object with sync status data if the node is syncing

* **startingBlock: QUANTITY** - The block at which the import started (will only be reset, after the sync reached his head)
* **currentBlock: QUANTITY** - The current block, same as eth\_blockNumber
* **highestBlock: QUANTITY** - The estimated highest block

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://zkfair.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": false,
    "id": 1
}
```
{% endcode %}
