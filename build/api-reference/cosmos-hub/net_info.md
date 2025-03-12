---
description: Get network info.
---

# /net\_info

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/net_info

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "listening": true,
        "listeners": [
            "Listener(@)"
        ],
        "n_peers": "10",
        "peers": [
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "72829b78b38408b03793ed389b9f16596b82c306",
                    "listen_addr": "tcp://146.59.81.92:26656",
                    "network": "cosmoshub-4",
                    "version": "v0.34.24",
                    "channels": "40202122233038606100",
                    "moniker": "chorus_sentry35",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "295419355069983",
                    "SendMonitor": {
                        "Start": "2023-02-18T20:51:25.5Z",
                        "Bytes": "4523001219",
                        "Samples": "873581",
                        "InstRate": "10710",
                        "CurRate": "2646",
                        "AvgRate": "15310",
                        "PeakRate": "1917500",
                        "BytesRem": "0",
                        "Duration": "295419280000000",
                        "Idle": "20000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-02-18T20:51:25.5Z",
                        "Bytes": "6327573228",
                        "Samples": "846748",
                        "InstRate": "90980",
                        "CurRate": "31557",
                        "AvgRate": "21419",
                        "PeakRate": "2966960",
                        "BytesRem": "0",
                        "Duration": "295419340000000",
                        "Idle": "20000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "Channels": [
                        {
                            "ID": 48,
                            "SendQueueCapacity": "1",
                            "SendQueueSize": "0",
                            "Priority": "5",
                            "RecentlySent": "84960"
                        },
                        {
                            "ID": 64,
                            "SendQueueCapacity": "1000",
                            "SendQueueSize": "0",
                            "Priority": "5",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 32,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "6",
                            "RecentlySent": "9559"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "45881"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "57638"
                        },
                        {
                            "ID": 35,
                            "SendQueueCapacity": "2",
                            "SendQueueSize": "0",
                            "Priority": "1",
                            "RecentlySent": "9"
                        },
                        {
                            "ID": 56,
                            "SendQueueCapacity": "1",
                            "SendQueueSize": "0",
                            "Priority": "6",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 96,
                            "SendQueueCapacity": "10",
                            "SendQueueSize": "0",
                            "Priority": "5",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 97,
                            "SendQueueCapacity": "10",
                            "SendQueueSize": "0",
                            "Priority": "3",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 0,
                            "SendQueueCapacity": "10",
                            "SendQueueSize": "0",
                            "Priority": "1",
                            "RecentlySent": "0"
                        }
                    ]
                },
                "remote_ip": "146.59.81.92"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "137f98c8e22965e672744a3f8909c0f4c8cffc53",
                    "listen_addr": "tcp://135.148.54.43:26656",
                    "network": "cosmoshub-4",
                    "version": "v0.34.24",
                    "channels": "40202122233038606100",
                    "moniker": "CD5D47E24AD0EF60472AF356B783AD28",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "428349193273595",
                    "SendMonitor": {
                        "Start": "2023-02-17T07:55:55.66Z",
                        "Bytes": "8197014766",
                        "Samples": "1307023",
                        "InstRate": "220900",
                        "CurRate": "29357",
                        "AvgRate": "19136",
                        "PeakRate": "2661100",
                        "BytesRem": "0",
                        "Duration": "428349120000000",
                        "Idle": "20000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-02-17T07:55:55.66Z",
                        "Bytes": "9126574578",
                        "Samples": "1169199",
                        "InstRate": "163229",
                        "CurRate": "32668",
                        "AvgRate": "21306",
                        "PeakRate": "2112271",
                        "BytesRem": "0",
                        "Duration": "428349200000000",
                        "Idle": "60000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "Channels": [
                        {
                            "ID": 48,
                            "SendQueueCapacity": "1",
                            "SendQueueSize": "0",
                            "Priority": "5",
                            "RecentlySent": "83376"
                        },
                        {
                            "ID": 64,
                            "SendQueueCapacity": "1000",
                            "SendQueueSize": "0",
                            "Priority": "5",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 32,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "6",
                            "RecentlySent": "9363"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "64885"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "79540"
                        },
                        {
                            "ID": 35,
                            "SendQueueCapacity": "2",
                            "SendQueueSize": "0",
                            "Priority": "1",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 56,
                            "SendQueueCapacity": "1",
                            "SendQueueSize": "0",
                            "Priority": "6",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 96,
                            "SendQueueCapacity": "10",
                            "SendQueueSize": "0",
                            "Priority": "5",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 97,
                            "SendQueueCapacity": "10",
                            "SendQueueSize": "0",
                            "Priority": "3",
                            "RecentlySent": "0"
                        },
                        {
                            "ID": 0,
                            "SendQueueCapacity": "10",
                            "SendQueueSize": "0",
                            "Priority": "1",
                            "RecentlySent": "0"
                        }
                    ]
                },
                "remote_ip": "135.148.54.43"
            },
            ......
        ]
    }
}
```
{% endcode %}
