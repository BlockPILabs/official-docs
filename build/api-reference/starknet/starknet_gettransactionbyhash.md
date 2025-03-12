---
description: Get the details and status of a submitted transaction
---

# starknet\_getTransactionByHash

#### **Parameters:**

**TRANSACTION\_HASH**  -  The hash of the requested transaction.

#### **Returns:**

A transaction object.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_getTransactionByHash","params":["0x23b5171f490079d5ba6314ebdce1dd5a1086fc2b07da7f7f51a62bd07671f6f"],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "calldata": [
            "0x1",
            "0x3c10537fa0073b2dd5120242697dbf76d6173eb9f384d3bf3d284d53388a0b0",
            "0x1f64d317ff277789ba74de95db50418ab0fa47c09241400b7379b50d6334c3a",
            "0x2",
            "0x957",
            "0x1"
        ],
        "max_fee": "0x24d1b70b87a74",
        "nonce": "0x6e0",
        "sender_address": "0x6984560836d038e6e42226351eb70e627afc7879df11aa3cfc383d41f6701a2",
        "signature": [
            "0x24119e51d81b0f73955e252e35db986b49962bef9316f36b4da126a7068fb9d",
            "0x69d2134ed551f9898105063a08bce4f2cfd69933e0a0073fee550ee1b39831b"
        ],
        "transaction_hash": "0x23b5171f490079d5ba6314ebdce1dd5a1086fc2b07da7f7f51a62bd07671f6f",
        "type": "INVOKE",
        "version": "0x1"
    }
}
```
{% endcode %}
