---
description: Returns additional zkSync-specific information about the L2 block.
---

# zks\_getBlockDetails

#### **Parameters:**

**block-uint32**, The number of the block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getBlockDetails", "params": [ 140599 ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "baseSystemContractsHashes": {
      "bootloader": "0x010007793a328ef16cc7086708f7f3292ff9b5eed9e7e539c184228f461bf4ef",
      "default_aa": "0x0100067d861e2f5717a12c3e869cfb657793b86bbb0caa05cc1421f16c5217bc"
    },
    "commitTxHash": "0xd045e3698f018cb233c3817eb53a41a4c5b28784ffe659da246aa33bda34350c",
    "committedAt": "2023-03-26T07:21:21.046817Z",
    "executeTxHash": "0xbb66aa75f437bb4255cf751badfc6b142e8d4d3a4e531c7b2e737a22870ff19e",
    "executedAt": "2023-03-27T07:44:52.187764Z",
    "l1BatchNumber": 1617,
    "l1GasPrice": 20690385511,
    "l1TxCount": 0,
    "l2FairGasPrice": 250000000,
    "l2TxCount": 20,
    "number": 140599,
    "operatorAddress": "0xfeee860e7aae671124e9a4e61139f3a5085dfeee",
    "proveTxHash": "0x1591e9b16ff6eb029cc865614094b2e6dd872c8be40b15cc56164941ed723a1a",
    "provenAt": "2023-03-26T19:48:35.200565Z",
    "rootHash": "0xf1adac176fc939313eea4b72055db0622a10bbd9b7a83097286e84e471d2e7df",
    "status": "verified",
    "timestamp": 1679815038
  },
  "id": 1
}


```
{% endcode %}
