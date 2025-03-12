---
description: Returns data of transactions in a block.
---

# zks\_getRawBlockTransactions

**Parameters:**

**block-uint32**, Block number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getRawBlockTransactions", "params": [ 5187 ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": [
    {
      "common_data": {
        "L1": {
          "canonicalTxHash": "0x22de7debaa98758afdaee89f447ff43bab5da3de6acca7528b281cc2f1be2ee9",
          "deadlineBlock": 0,
          "ethBlock": 16751339,
          "ethHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "fullFee": "0x0",
          "gasLimit": "0x989680",
          "gasPerPubdataLimit": "0x320",
          "layer2TipFee": "0x0",
          "maxFeePerGas": "0x0",
          "opProcessingType": "Common",
          "priorityQueueType": "Deque",
          "refundRecipient": "0x87869cb87c4fa78ca278df358e890ff73b42a39e",
          "sender": "0x87869cb87c4fa78ca278df358e890ff73b42a39e",
          "serialId": 67,
          "toMint": "0x0"
        }
      },
      "execute": {
        "calldata": "0x471c46c800000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000100000000000000000000000031edd5a882583cbf3a712e98e100ef34ad6934b400000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001",
        "contractAddress": "0xfc5b07a5dd1b80cf271d35642f75cc0500ff1e2c",
        "factoryDeps": [],
        "value": "0x0"
      },
      "received_timestamp_ms": 1677887544169
    }
  ],
  "id": 1
}
```
{% endcode %}
