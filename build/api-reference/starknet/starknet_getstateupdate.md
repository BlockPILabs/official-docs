---
description: Get the information about the result of executing the requested block
---

# starknet\_getStateUpdate

#### **Parameters:**

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`

#### **Returns:**

The information about the state update of the requested block

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getStateUpdate","params":["latest"],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "block_hash": "0x7a7be174b3ea3e3f77085bccdd5de3adf5346a57fd09435bdac071fa8b154dd",
        "new_root": "0x1c09e179ad75a8fa679fbe067f382a87dc8fa5abdef90a6e508e4bd6d3aa0a0",
        "old_root": "0x1f8106a59254bc7e44d1b25ba1d40ea232f6007c2f2bda3e43d8a1b41213227",
        "state_diff": {
            "declared_classes": [],
            "deployed_contracts": [
                {
                    "address": "0x11add4872c00cefe53107eb579af2266ccdb298bf580bf8be9bd76d8b3685ae",
                    "class_hash": "0x3530cc4759d78042f1b543bf797f5f3d647cde0388c33734cf91b7f7b9314a9"
                },
                {
                    "address": "0x11cfb4b8ca4c0a88f1e4aeadbdfc1a542a04341528b88afcb6f8e50953d5c41",
                    "class_hash": "0x3530cc4759d78042f1b543bf797f5f3d647cde0388c33734cf91b7f7b9314a9"
                },
                ......
}
```
{% endcode %}
