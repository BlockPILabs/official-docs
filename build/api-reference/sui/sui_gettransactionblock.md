---
description: Return the transaction response object.
---

# sui\_getTransactionBlock

#### **Parameters:**

**digest< TransactionDigest** > - The digest of the queried transaction&#x20;

**options< TransactionBlockResponseOptions >** - Options for specifying the content to be returned

#### **Returns:**

SuiTransactionBlockResponse< TransactionBlockResponse >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getTransactionBlock",
  "params": [
    "FngHthKGR852Y6tUU57UPLDzqFyKLyJ5EfwinSzVYEYn",
    {
      "showInput": true,
      "showRawInput": false,
      "showEffects": true,
      "showEvents": true,
      "showObjectChanges": false,
      "showBalanceChanges": false,
      "showRawEffects": false
    }
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "digest": "FngHthKGR852Y6tUU57UPLDzqFyKLyJ5EfwinSzVYEYn",
        "transaction": {
            "data": {
                "messageVersion": "v1",
                "transaction": {
                    "kind": "ProgrammableTransaction",
                    "inputs": [
                        {
                            "type": "object",
                            "objectType": "sharedObject",
                            "objectId": "0x4846a1f1030deffd9dea59016402d832588cf7e0c27b9e4c1a63d2b5e152873a",
                            "initialSharedVersion": "87426356",
                            "mutable": true
                        },
                        {
                            "type": "object",
                            "objectType": "sharedObject",
                            "objectId": "0x0000000000000000000000000000000000000000000000000000000000000006",
                            "initialSharedVersion": "1",
                            "mutable": false
                        }
                    ],
                    "transactions": [
                    ......
```
{% endcode %}
