---
description: Returns data pertaining to a given batch.
---

# zks\_getL1BatchDetails

**Parameters:**

**batch-L1BatchNumber**, The layer 1 batch number.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getL1BatchDetails", "params": [ 12345 ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "baseSystemContractsHashes": {
      "bootloader": "0x010007793a328ef16cc7086708f7f3292ff9b5eed9e7e539c184228f461bf4ef",
      "default_aa": "0x0100067d861e2f5717a12c3e869cfb657793b86bbb0caa05cc1421f16c5217bc"
    },
    "commitTxHash": "0xe5e76d1e17cff2b7232d40ddf43c245e29c76e5354571aa8083d73e793efb64a",
    "committedAt": "2023-04-09T18:05:40.548203Z",
    "executeTxHash": "0x19c125a6104f731bcc1ce378f090c808e97c6d634fc32cb786694a94fc8219a1",
    "executedAt": "2023-04-10T18:48:25.009708Z",
    "l1GasPrice": 29424338466,
    "l1TxCount": 9,
    "l2FairGasPrice": 250000000,
    "l2TxCount": 294,
    "number": 12345,
    "proveTxHash": "0xe980f58feed22a4dbc46fe0339bfcbc09f51c99b2f3bc4f9f60e710ea5f0a2da",
    "provenAt": "2023-04-09T22:51:16.200810Z",
    "rootHash": "0x994d2738f7ac89b45c8381a7816307b501c00b3127afc79e440dbf1b3e3b5a8c",
    "status": "verified",
    "timestamp": 1681063384
  },
  "id": 1
}



```
{% endcode %}
