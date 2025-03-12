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
curl  https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "currentBlock": "0x208f2a8",
        "healedBytecodeBytes": "0x0",
        "healedBytecodes": "0x0",
        "healedTrienodeBytes": "0x0",
        "healedTrienodes": "0x0",
        "healingBytecode": "0x0",
        "healingTrienodes": "0x0",
        "highestBlock": "0x2094136",
        "startingBlock": "0x2083016",
        "syncedAccountBytes": "0x0",
        "syncedAccounts": "0x0",
        "syncedBytecodeBytes": "0x0",
        "syncedBytecodes": "0x0",
        "syncedStorage": "0x0",
        "syncedStorageBytes": "0x0"
    }
}
```
{% endcode %}
