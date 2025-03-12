---
description: >-
  Get Tendermint status including node info, pubkey, latest block hash, app
  hash, block height and time.
---

# /status

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/status

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "node_info": {
            "protocol_version": {
                "p2p": "8",
                "block": "11",
                "app": "0"
            },
            "id": "99ac377d924860cab400da062472bd9c3446c9f8",
            "listen_addr": "tcp://0.0.0.0:31440",
            "network": "cosmoshub-4",
            "version": "v0.34.24",
            "channels": "40202122233038606100",
            "moniker": "blockpi",
            "other": {
                "tx_index": "on",
                "rpc_address": "tcp://0.0.0.0:31441"
            }
        },
        "sync_info": {
            "latest_block_hash": "A26FA8C5C46967C8BB58E92DC66CC89CB99E12A5CA4A649A60B0FE83A51C2E1B",
            "latest_app_hash": "FDDFE292D639C2D780D9DD5FF49294F1F4FB9B4BA1B0C43D25535D931098D96E",
            "latest_block_height": "14183736",
            "latest_block_time": "2023-02-22T06:53:22.427165053Z",
            "earliest_block_hash": "8535EF9A5E4D23CFA774DB2F3B71A3C67ECF6C3634687ECD479FC98C0ADE80BD",
            "earliest_app_hash": "E8B616E41205D8D75584177E4FCED2AB9D4EDD34CBAB099AB14CCB823AFE740A",
            "earliest_block_height": "13679694",
            "earliest_block_time": "2023-01-15T11:44:44.127906024Z",
            "catching_up": false
        },
        "validator_info": {
            "address": "AF8A7EAE5265A8A51E1F8573E9E77FCA1796F752",
            "pub_key": {
                "type": "tendermint/PubKeyEd25519",
                "value": "eV90ruKgLlWu4yHY4oJ+DlFo/j+q61Sb4HJ45QgAG6E="
            },
            "voting_power": "0"
        }
    }
}
```
{% endcode %}
