---
description: Returns data from a specific transaction given by the transaction hash.
---

# zks\_getTransactionDetails

**Parameters:**

**hash-H256**, Transaction hash as string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getTransactionDetails", "params": [ "0x22de7debaa98758afdaee89f447ff43bab5da3de6acca7528b281cc2f1be2ee9"]}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "ethCommitTxHash": "0x3da5b6eda357189c9243c41c5a33b1b2ed0169be172705d74681a25217702772",
    "ethExecuteTxHash": "0xdaff5fd7ff91333b161de54534b4bb6a78e5325329959a0863bf0aae2b0fdcc6",
    "ethProveTxHash": "0x2f482d3ea163f5be0c2aca7819d0beb80415be1a310e845a2d726fbc4ac54c80",
    "fee": "0x0",
    "gasPerPubdata": "0x320",
    "initiatorAddress": "0x87869cb87c4fa78ca278df358e890ff73b42a39e",
    "isL1Originated": true,
    "receivedAt": "2023-03-03T23:52:24.169Z",
    "status": "verified"
  },
  "id": 1
}
```
{% endcode %}
