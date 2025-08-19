---
description: Return paginated list of checkpoints
---

# sui\_getCheckpoints

#### **Parameters:**

**cursor< BigInt\_for\_uint64 >** - An optional paging cursor. If provided, the query will start from the next item after the specified cursor. Default to start from the first item if not specified.&#x20;

**limit< uint >** - Maximum item returned per page, default to \[QUERY\_MAX\_RESULT\_LIMIT\_CHECKPOINTS] if not specified.&#x20;

**descending\_order< Boolean >** - Query result ordering, default to false (ascending order), oldest record first.

#### **Returns:**

CheckpointPage< Page\_for\_Checkpoint\_and\_BigInt\_for\_uint64 >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getCheckpoints",
  "params": [
    "1004",
    4,
    false
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "data": [
            {
                "epoch": "0",
                "sequenceNumber": "1005",
                "digest": "9chFiCFNmdogdDjRBpWfe1GdfVrN8GV2GUyTdNrQkqe",
                "networkTotalTransactions": "1006",
                "previousDigest": "9kcQj1qymuGAFHrAdPRaDF2MkeiGwnXwuTp5dboYXTN",
                "epochRollingGasCostSummary": {
                    "computationCost": "0",
                    "storageCost": "0",
                    "storageRebate": "0",
                    "nonRefundableStorageFee": "0"
                },
                "timestampMs": "1681393667576",
                "transactions": [
                    "9wpiZnYRTNkCaPLuVqQ6W2jEH26tHkKzu4JRjxYW2y5o"
                ],
                "checkpointCommitments": [],
                "validatorSignature": "i3MtXlu/r7aRWkpg/H3gd1olPJlSLRPx3ByJsN2UNDJazQA0wwhKbBCr7YMw44Pg"
            },
            ......
```
{% endcode %}
