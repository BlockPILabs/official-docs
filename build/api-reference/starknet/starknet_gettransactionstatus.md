---
description: >-
  Gets the transaction status (possibly reflecting that the tx is still in the
  mempool, or dropped from it)
---

# starknet\_getTransactionStatus

#### **Parameters:**

**Transaction hash** - string, The transaction hash, as assigned in StarkNet

#### **Returns:**

Transaction finality status and execution status

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getTransactionStatus","params":["0x23b5171f490079d5ba6314ebdce1dd5a1086fc2b07da7f7f51a62bd07671f6f"],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "execution_status": "SUCCEEDED",
        "finality_status": "ACCEPTED_ON_L2"
    }
}
```
{% endcode %}
