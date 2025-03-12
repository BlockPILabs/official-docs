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
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/status

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
            "id": "624f24d16ee7910d9256650a2be901a0efdfbc0b",
            "listen_addr": "5.161.116.76:26656",
            "network": "athens_7001-1",
            "version": "0.34.23",
            "channels": "40202122233038606100",
            "moniker": "mynode",
            "other": {
                "tx_index": "on",
                "rpc_address": "tcp://0.0.0.0:31461"
            }
        },
        "sync_info": {
            "latest_block_hash": "AC6FAD20ED26BF93A98EACC2146BA4CA8E406F898BA4ED18A192D1ABA1E0DD01",
            "latest_app_hash": "38C8D7610C5764D2EDDB51D64436738D6C8FD0B204A2FC16C895AC72E0DDBD36",
            "latest_block_height": "2115573",
            "latest_block_time": "2023-03-31T06:35:19.421112981Z",
            "earliest_block_hash": "314B2ACE2A35B0ADB608706491D874C33ECE3A744C035D41F032C6198E902651",
            "earliest_app_hash": "60234ECAC8940E1D62C81DEF69553B2AAEB32DF59B009946FC687A8B43E180BF",
            "earliest_block_height": "1191001",
            "earliest_block_time": "2023-02-02T03:11:43.782407466Z",
            "catching_up": false
        },
        "validator_info": {
            "address": "B6EA71ADDDF1310E9C0B5BDE67C78C4EA15A91B8",
            "pub_key": {
                "type": "tendermint/PubKeyEd25519",
                "value": "j0tK2fWA3e5U8p38pGepai0M9ZNIhoVVEoTHtcXfcJs="
            },
            "voting_power": "0"
        }
    }
}
```
{% endcode %}
