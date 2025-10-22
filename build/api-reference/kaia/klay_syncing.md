---
description: Returns an object with data about the sync status or false.
---

# kaia\_syncing

#### **Parameters**

None

#### **Return Value**

`Object|Boolean`, an object with sync status data or `false` when not syncing:

| Name          | Type     | Description                                                                                                       |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| startingBlock | QUANTITY | The block at which the import started (will only be reset, after the sync reached his head).                      |
| currentBlock  | QUANTITY | The current block, same as `klay_blockNumber`.                                                                    |
| highestBlock  | QUANTITY | The estimated highest block.                                                                                      |
| pulledStates  | QUANTITY | The number of state entries processed until now. If the sync mode is not "fast", zero is returned.                |
| knownStates   | QUANTITY | The number of known state entries that still need to be pulled. If the sync mode is not "fast", zero is returned. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_syncing","params":[],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": {
    "currentBlock":"0x3e31e",
    "highestBlock":"0x827eef",
    "knownStates":"0x0",
    "pulledStates":"0x0",
    "startingBlock":"0x0"
  }
}
// Or when not syncing
{
  "jsonrpc": "2.0",
  "id":1,
  "result": false
}
```
{% endcode %}
