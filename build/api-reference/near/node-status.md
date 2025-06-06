---
description: >-
  Returns general status of a given node (sync status, nearcore node version,
  protocol version, etc), and the current set of validators.
---

# Node Status

* method: `status`
* params: `[]`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "status",
  "params": []
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "version": {
      "version": "1.14.0-rc.1",
      "build": "effa3b7a-modified"
    },
    "chain_id": "testnet",
    "protocol_version": 35,
    "latest_protocol_version": 35,
    "rpc_addr": "0.0.0.0:3030",
    "validators": [
      {
        "account_id": "node3",
        "is_slashed": false
      },
      {
        "account_id": "node0",
        "is_slashed": false
      },
      {
        "account_id": "staked.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "01node.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "node2",
        "is_slashed": false
      },
      {
        "account_id": "dokia.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "node1",
        "is_slashed": false
      },
      {
        "account_id": "lowfeevalidation.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "sl1sub.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "zainy.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "chorus-one.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "thepassivetrust.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "certusone.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "joe1.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "bisontrails.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "valeraverim.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "lunanova.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "bazilik.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "dsrvlabs.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "kronos.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "nodeasy.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "kytzu.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "bitcat.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "pool_easy2stake.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "fresh_lockup.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "staking-power.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "syncnode.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "inotel.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "zpool.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "aquarius.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "cloudpost.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "staked.pool.6fb1358",
        "is_slashed": false
      },
      {
        "account_id": "moonlet.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "jazza.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "orangeclub.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "blazenet.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "pathrock.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "stakin.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "northernlights.stakingpool",
        "is_slashed": false
      },
      {
        "account_id": "alexandruast.pool.f863973.m0",
        "is_slashed": false
      },
      {
        "account_id": "top.pool.f863973.m0",
        "is_slashed": false
      }
    ],
    "sync_info": {
      "latest_block_hash": "44kieHwr7Gg5r72V3DgU7cpgV2aySkk5qbBCdvwens8T",
      "latest_block_height": 17774278,
      "latest_state_root": "3MD3fQqnm3JYa9UQgenEJsR6UHoWuHV4Tpr4hZY7QwfY",
      "latest_block_time": "2020-09-27T23:59:38.008063088Z",
      "syncing": false
    },
    "validator_account_id": "nearup-node8"
  },
  "id": "dontcare"
}
```
{% endcode %}
