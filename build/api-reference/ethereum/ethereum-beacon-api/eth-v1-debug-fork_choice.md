---
description: Retrieves all current fork choice context.
---

# /eth/v1/debug/fork\_choice



#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/debug/fork_choice

// Result
{
    "justified_checkpoint": {
        "epoch": "284095",
        "root": "0x720f7070c7e1953cd6e30f041c8dec6ffbdebc8e318fe9642fe2777aa41f7398"
    },
    "finalized_checkpoint": {
        "epoch": "284094",
        "root": "0x95e5f0387df3e314485e0e3cea118d9f8026d10e8005779d17e0789a09a4a75f"
    },
    "fork_choice_nodes": [
        {
            "slot": "9090912",
            "block_root": "0x3777bace92e30a1476efcc34d0c0ee1d0d9431bdf7b2444ea259b5baa9fbb390",
            "parent_root": null,
            "justified_epoch": "284090",
            "finalized_epoch": "284089",
            "weight": "32589203725000000",
            "validity": "valid",
            "execution_block_hash": "0xfca6962556bab42153e4c4dca938f53f4ed5140f6966da165b41d9167dd467b1"
        },
        ......
```
{% endcode %}
