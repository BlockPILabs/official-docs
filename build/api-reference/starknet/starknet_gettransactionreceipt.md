---
description: Get the transaction receipt by the transaction hash
---

# starknet\_getTransactionReceipt

#### **Parameters:**

**TRANSACTION\_HASH**  -  The hash of the requested transaction

#### **Returns:**

A transaction receipt object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_getTransactionReceipt","params": ["0x23b5171f490079d5ba6314ebdce1dd5a1086fc2b07da7f7f51a62bd07671f6f"],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "actual_fee": "0x12fb985cd5220",
        "block_hash": "0x33a6f50845330fdf2a3bd2deaa69c88f5569566151be440e653adb79c8c76c0",
        "block_number": 472393,
        "events": [
            {
                "data": [
                    "0x6984560836d038e6e42226351eb70e627afc7879df11aa3cfc383d41f6701a2",
                    "0x957",
                    ......
}
```
{% endcode %}
