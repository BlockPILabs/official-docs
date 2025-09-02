---
description: Return a checkpoint
---

# sui\_getCheckpoint

#### **Parameters:**

**id< CheckpointId >** - Checkpoint identifier, can use either checkpoint digest, or checkpoint sequence number as input.

#### **Returns:**

Checkpoint< Checkpoint >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getCheckpoint",
  "params": [
    "1000"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "epoch": "0",
        "sequenceNumber": "1000",
        "digest": "BE4JixC94sDtCgHJZruyk7QffZnWDFvM2oFjC8XtChET",
        "networkTotalTransactions": "1001",
        "previousDigest": "41nPNZWHvvajmBQjX3GbppsgGZDEB6DhN4UxPkjSYRRj",
        "epochRollingGasCostSummary": {
            "computationCost": "0",
            "storageCost": "0",
            "storageRebate": "0",
            "nonRefundableStorageFee": "0"
        },
        "timestampMs": "1681393657483",
        "transactions": [
            "9NnjyPG8V2TPCSbNE391KDyge42AwV3vUD7aNtQQ9eqS"
        ],
        "checkpointCommitments": [],
        "validatorSignature": "r8/5+Rm7niIlndcnvjSJ/vZLPrH3xY/ePGYTvrVbTascoQSpS+wsGlC+bQBpzIwA"
    },
    "id": 1
}
```
{% endcode %}
