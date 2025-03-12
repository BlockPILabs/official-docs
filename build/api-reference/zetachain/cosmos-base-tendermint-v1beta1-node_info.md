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
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/base/tendermint/v1beta1/node_info
// Result
{
    "default_node_info": {
        "protocol_version": {
            "p2p": "8",
            "block": "11",
            "app": "0"
        },
        "default_node_id": "624f24d16ee7910d9256650a2be901a0efdfbc0b",
        "listen_addr": "5.161.116.76:26656",
        "network": "athens_7001-1",
        "version": "0.34.23",
        "channels": "QCAhIiMwOGBhAA==",
        "moniker": "mynode",
        "other": {
            "tx_index": "on",
            "rpc_address": "tcp://0.0.0.0:31461"
        }
    },
    "application_version": {
        "name": "zetacore",
        "app_name": "<appd>",
        "version": "athens2-v1.1.10",
        "git_commit": "acc75eaf24af65b2393b339587ca14722ed84fb7",
        "build_tags": "",
        "go_version": "go version go1.18.10 linux/amd64",
        "build_deps": [
            {
                "path": "cosmossdk.io/math",
                "version": "v1.0.0-beta.3",
                "sum": "h1:TbZxSopz2LqjJ7aXYfn7nJSb8vNaBklW6BLpcei1qwM="
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
