---
description: The properties of the connected node
---

# /node\_info

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/node_info

// Result
{
    "node_info": {
        "protocol_version": {
            "p2p": "8",
            "block": "11",
            "app": "0"
        },
        "id": "effc008dee70b05eb33e27b3ec7d78a3032ef001",
        "listen_addr": "tcp://0.0.0.0:31440",
        "network": "cosmoshub-4",
        "version": "v0.34.25",
        "channels": "40202122233038606100",
        "moniker": "nodeasy",
        "other": {
            "tx_index": "on",
            "rpc_address": "tcp://0.0.0.0:31441"
        }
    },
    "application_version": {
        "name": "gaia",
        "server_name": "gaiad",
        "version": "v7.1.1",
        "commit": "b2504c1e28eae936477c7b06ae4c0f058613a4e8",
        "build_tags": "netgo ledger,",
        "go": "go version go1.18.5 linux/amd64",
        "build_deps": [
            "filippo.io/edwards25519@v1.0.0-beta.2",
            "github.com/99designs/keyring@v1.1.6",
             ......
            "google.golang.org/genproto@v0.0.0-20221014213838-99cd37c6964a",
            "google.golang.org/grpc@v1.50.1 => google.golang.org/grpc@v1.33.2",
            "google.golang.org/protobuf@v1.28.2-0.20220831092852-f930b1dc76e8",
            "gopkg.in/ini.v1@v1.67.0",
            "gopkg.in/yaml.v2@v2.4.0",
            "gopkg.in/yaml.v3@v3.0.1",
            "nhooyr.io/websocket@v1.8.6"
        ],
        "cosmos_sdk_version": "v0.45.9"
    }
}
```
{% endcode %}
