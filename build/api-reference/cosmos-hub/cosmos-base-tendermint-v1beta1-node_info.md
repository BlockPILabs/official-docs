---
description: GetNodeInfo queries the current node info.
---

# /cosmos/base/tendermint/v1beta1/node\_info

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/base/tendermint/v1beta1/node_info
// Result
{
    "default_node_info": {
        "protocol_version": {
            "p2p": "8",
            "block": "11",
            "app": "0"
        },
        "default_node_id": "effc008dee70b05eb33e27b3ec7d78a3032ef001",
        "listen_addr": "tcp://0.0.0.0:31440",
        "network": "cosmoshub-4",
        "version": "v0.34.25",
        "channels": "QCAhIiMwOGBhAA==",
        "moniker": "nodeasy",
        "other": {
            "tx_index": "on",
            "rpc_address": "tcp://0.0.0.0:31441"
        }
    },
    "application_version": {
        "name": "gaia",
        "app_name": "gaiad",
        "version": "v7.1.1",
        "git_commit": "b2504c1e28eae936477c7b06ae4c0f058613a4e8",
        "build_tags": "netgo ledger,",
        "go_version": "go version go1.18.5 linux/amd64",
        "build_deps": [
            {
                "path": "filippo.io/edwards25519",
                "version": "v1.0.0-beta.2",
                "sum": "h1:/BZRNzm8N4K4eWfK28dL4yescorxtO7YG1yun8fy+pI="
            },
            {
                "path": "github.com/99designs/keyring",
                "version": "v1.1.6",
                "sum": "h1:kVDC2uCgVwecxCk+9zoCt2uEL6dt+dfVzMvGgnVcIuM="
            },
            ......
            {
                "path": "nhooyr.io/websocket",
                "version": "v1.8.6",
                "sum": "h1:s+C3xAMLwGmlI31Nyn/eAehUlZPwfYZu2JXM621Q5/k="
            }
        ],
        "cosmos_sdk_version": "v0.45.9"
    }
}
```
{% endcode %}
