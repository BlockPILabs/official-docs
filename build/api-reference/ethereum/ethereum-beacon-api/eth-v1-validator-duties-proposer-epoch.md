---
description: Returns node health status in http status codes. Useful for load balancers.
---

# /eth/v1/validator/duties/proposer/{epoch}

Request beacon node to provide all validators that are scheduled to propose a block in the given epoch. Duties should only need to be checked once per epoch, however a chain reorganization could occur that results in a change of duties. For full safety, you should monitor head events and confirm the dependent root in this response matches:

* event.current\_duty\_dependent\_root when `compute_epoch_at_slot(event.slot) == epoch`
* event.block otherwise

The dependent\_root value is `get_block_root_at_slot(state, compute_start_slot_at_epoch(epoch) - 1)` or the genesis block root in the case of underflow.

#### Parameters:

**epoch-string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/duties/proposer/284100

// Result
{
    "dependent_root": "0xcc0c52cb6aaee9b211c2bbaf28b46faee7517bc6c358db63c07a017fb0e2f612",
    "execution_optimistic": false,
    "data": [
        {
            "pubkey": "0x91136da11e4179a276956fc89f1380264a4689728ec6ee509fb254d10d2d49a16353f042cf9d0f141d385118fe05f32f",
            "validator_index": "833889",
            "slot": "9091200"
        },
        ......
```
{% endcode %}
