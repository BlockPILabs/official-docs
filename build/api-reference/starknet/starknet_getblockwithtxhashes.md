---
description: Get block information with transaction hashes given the block id
---

# starknet\_getBlockWithTxHashes

#### **Parameters:**

**BLOCK\_PARAM** -  Expected one of `block_number`, `block_hash`, `latest`, `pending`.

#### **Returns:**

The resulting block information with transaction hashes.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getBlockWithTxHashes","params":["latest"],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "block_hash": "0x1767074c2ac8f6e6a704682dacaa7b9dfb1aee0c98cedf48de0619541bcdd6",
        "block_number": 472386,
        "l1_gas_price": {
            "price_in_wei": "0xa21580404"
        },
        "new_root": "0x4133fef4768a0f4f4597f847149a77befa769b48e1c67bfe535166c80df060d",
        "parent_hash": "0x385de00666cc0ccb2f2014639239e8a105d77cc00b0a7cfa270a57cf7b4fc7",
        "sequencer_address": "0x1176a1bd84444c89232ec27754698e5d2e7e1a7f1539f12027f28b23ec9f3d8",
        "starknet_version": "0.12.2",
        "status": "ACCEPTED_ON_L2",
        "timestamp": 1702868020,
        "transactions": [
            "0x27a3d263159c5db3de1366ef596e1359040ff86d991bfe016b54c9f971fdc25",
            .....
}
```
{% endcode %}
