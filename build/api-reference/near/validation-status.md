---
description: >-
  Queries active validators on the network returning details and the state of
  validation on the blockchain.
---

# Validation Status

* method: `validators`
* params: `["block hash"]`, `[block number]`, `{"epoch_id": "epoch id"}`, `{"block_id": block number}`, `{"block_id": "block hash"}`, or `[null]` for the latest block

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "validators",
  "params": [17791098]
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "current_validators": [
      {
        "account_id": "01node.pool.f863973.m0",
        "public_key": "ed25519:3iNqnvBgxJPXCxu6hNdvJso1PEAc1miAD35KQMBCA3aL",
        "is_slashed": false,
        "stake": "176429739989396285019500901780",
        "shards": [0],
        "num_produced_blocks": 213,
        "num_expected_blocks": 213
      },
      ......
```
{% endcode %}
