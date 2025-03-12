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
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/health

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "listening": true,
        "listeners": [
            "Listener(@5.161.116.76:26656)"
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
                    "id": "d046a7d785accd74bb0d7b4405749ed6b3280e92",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "HashQuark",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://127.0.0.1:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "171798371020672",
                    "SendMonitor": {
                        "Start": "2023-03-29T06:52:49.44Z",
                        "Bytes": "1351758854",
                        "Samples": "557834",
                        "InstRate": "5621",
                        "CurRate": "6036",
                        "AvgRate": "7868",
                        "PeakRate": "5131240",
                        "BytesRem": "0",
                        "Duration": "171798380000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-29T06:52:49.44Z",
                        "Bytes": "1640271726",
                        "Samples": "555594",
                        "InstRate": "11071",
                        "CurRate": "19281",
                        "AvgRate": "9548",
                        "PeakRate": "5126840",
                        "BytesRem": "0",
                        "Duration": "171798380000000",
                        "Idle": "140000000",
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
                            "RecentlySent": "53742"
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
                            "RecentlySent": "871"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "49572"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "2819"
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
                "remote_ip": "152.32.150.236"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "f04cfca9b9fc8e0d5c0083dad20ab9a0fefba505",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "validator0",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91902751754583",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:04:25.06Z",
                        "Bytes": "655522912",
                        "Samples": "306075",
                        "InstRate": "5621",
                        "CurRate": "5490",
                        "AvgRate": "7133",
                        "PeakRate": "1826490",
                        "BytesRem": "0",
                        "Duration": "91902760000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:04:25.06Z",
                        "Bytes": "1125259177",
                        "Samples": "354515",
                        "InstRate": "11075",
                        "CurRate": "19522",
                        "AvgRate": "12244",
                        "PeakRate": "1762810",
                        "BytesRem": "0",
                        "Duration": "91902720000000",
                        "Idle": "40000000",
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
                            "RecentlySent": "41971"
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
                            "RecentlySent": "869"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "35323"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3939"
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
                "remote_ip": "34.194.62.47"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "3b148cee21f6a16d53dd7799249afe6f844f7f3c",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "validator3",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91878369036809",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:04:49.46Z",
                        "Bytes": "668001146",
                        "Samples": "328498",
                        "InstRate": "7750",
                        "CurRate": "5753",
                        "AvgRate": "7270",
                        "PeakRate": "1676090",
                        "BytesRem": "0",
                        "Duration": "91878360000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:04:49.46Z",
                        "Bytes": "1124333839",
                        "Samples": "355589",
                        "InstRate": "11660",
                        "CurRate": "18433",
                        "AvgRate": "12237",
                        "PeakRate": "1340380",
                        "BytesRem": "0",
                        "Duration": "91878360000000",
                        "Idle": "100000000",
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
                            "RecentlySent": "48746"
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
                            "RecentlySent": "833"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "30760"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3050"
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
                "remote_ip": "54.144.102.58"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "950820f9568b346cb74cd92b2723ea919dc4401b",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "archive3",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91878368684736",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:04:49.46Z",
                        "Bytes": "899274686",
                        "Samples": "354617",
                        "InstRate": "7444",
                        "CurRate": "6320",
                        "AvgRate": "9788",
                        "PeakRate": "1930420",
                        "BytesRem": "0",
                        "Duration": "91878360000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:04:49.46Z",
                        "Bytes": "1107855231",
                        "Samples": "357263",
                        "InstRate": "15500",
                        "CurRate": "18616",
                        "AvgRate": "12058",
                        "PeakRate": "1378380",
                        "BytesRem": "0",
                        "Duration": "91878360000000",
                        "Idle": "100000000",
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
                            "RecentlySent": "53304"
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
                            "RecentlySent": "833"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "44000"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3008"
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
                "remote_ip": "44.196.5.6"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "730e0a4b91eda7e041f866b6342bb5fa7178d0b0",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "api1",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91878368556754",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:04:49.46Z",
                        "Bytes": "904798578",
                        "Samples": "356466",
                        "InstRate": "5621",
                        "CurRate": "6521",
                        "AvgRate": "9848",
                        "PeakRate": "1674080",
                        "BytesRem": "0",
                        "Duration": "91878360000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:04:49.46Z",
                        "Bytes": "1112549363",
                        "Samples": "357743",
                        "InstRate": "12917",
                        "CurRate": "18298",
                        "AvgRate": "12109",
                        "PeakRate": "1367820",
                        "BytesRem": "0",
                        "Duration": "91878360000000",
                        "Idle": "120000000",
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
                            "RecentlySent": "53719"
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
                            "RecentlySent": "784"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "31277"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3699"
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
                "remote_ip": "44.210.204.28"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "a417c375685afb97b7210d4c101c835521572731",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "archive0",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91844381551447",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:05:23.44Z",
                        "Bytes": "906436423",
                        "Samples": "355234",
                        "InstRate": "9950",
                        "CurRate": "6633",
                        "AvgRate": "9869",
                        "PeakRate": "1935280",
                        "BytesRem": "0",
                        "Duration": "91844380000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:05:23.44Z",
                        "Bytes": "1099646388",
                        "Samples": "340055",
                        "InstRate": "15500",
                        "CurRate": "17984",
                        "AvgRate": "11973",
                        "PeakRate": "1368350",
                        "BytesRem": "0",
                        "Duration": "91844380000000",
                        "Idle": "100000000",
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
                            "RecentlySent": "53895"
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
                            "RecentlySent": "773"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "48792"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3738"
                        },
                        {
                            "ID": 35,
                            "SendQueueCapacity": "2",
                            "SendQueueSize": "0",
                            "Priority": "1",
                            "RecentlySent": "7"
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
                "remote_ip": "35.170.251.63"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "845ad4617af8c97942261d6f0b3de78104994ef2",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "archive1",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91844127632910",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:05:23.7Z",
                        "Bytes": "903273304",
                        "Samples": "355399",
                        "InstRate": "7444",
                        "CurRate": "18361",
                        "AvgRate": "9835",
                        "PeakRate": "1604910",
                        "BytesRem": "0",
                        "Duration": "91844120000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:05:23.7Z",
                        "Bytes": "1101512520",
                        "Samples": "340538",
                        "InstRate": "31214",
                        "CurRate": "20419",
                        "AvgRate": "11993",
                        "PeakRate": "1733830",
                        "BytesRem": "0",
                        "Duration": "91844080000000",
                        "Idle": "40000000",
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
                            "RecentlySent": "51617"
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
                            "RecentlySent": "779"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "66428"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3732"
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
                "remote_ip": "44.212.168.142"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "e2551106be2ccd47fa4e963e1899297d8dfa07c8",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "validator2",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91038369472490",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:18:49.44Z",
                        "Bytes": "782590522",
                        "Samples": "316346",
                        "InstRate": "5621",
                        "CurRate": "5840",
                        "AvgRate": "8596",
                        "PeakRate": "1499770",
                        "BytesRem": "0",
                        "Duration": "91038380000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:18:49.44Z",
                        "Bytes": "1103987433",
                        "Samples": "350581",
                        "InstRate": "15500",
                        "CurRate": "18992",
                        "AvgRate": "12127",
                        "PeakRate": "1605767",
                        "BytesRem": "0",
                        "Duration": "91038380000000",
                        "Idle": "100000000",
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
                            "RecentlySent": "39765"
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
                            "RecentlySent": "784"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "33640"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3499"
                        },
                        {
                            "ID": 35,
                            "SendQueueCapacity": "2",
                            "SendQueueSize": "0",
                            "Priority": "1",
                            "RecentlySent": "12"
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
                "remote_ip": "52.206.155.197"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "31c9f21b3dff1167993d4291479d8381f59d3dc4",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "archive2",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "91548370576988",
                    "SendMonitor": {
                        "Start": "2023-03-30T05:10:19.44Z",
                        "Bytes": "889248090",
                        "Samples": "350227",
                        "InstRate": "5621",
                        "CurRate": "18584",
                        "AvgRate": "9713",
                        "PeakRate": "1596790",
                        "BytesRem": "0",
                        "Duration": "91548380000000",
                        "Idle": "140000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T05:10:19.44Z",
                        "Bytes": "1108830047",
                        "Samples": "361192",
                        "InstRate": "15500",
                        "CurRate": "19340",
                        "AvgRate": "12112",
                        "PeakRate": "1372030",
                        "BytesRem": "0",
                        "Duration": "91548380000000",
                        "Idle": "100000000",
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
                            "RecentlySent": "53280"
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
                            "RecentlySent": "833"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "67245"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3935"
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
                "remote_ip": "18.213.164.140"
            },
            {
                "node_info": {
                    "protocol_version": {
                        "p2p": "8",
                        "block": "11",
                        "app": "0"
                    },
                    "id": "d432b334542ee3943c2258b76bf90dd0180c5d5b",
                    "listen_addr": "tcp://0.0.0.0:26656",
                    "network": "athens_7001-1",
                    "version": "0.34.23",
                    "channels": "40202122233038606100",
                    "moniker": "validator4",
                    "other": {
                        "tx_index": "on",
                        "rpc_address": "tcp://0.0.0.0:26657"
                    }
                },
                "is_outbound": true,
                "connection_status": {
                    "Duration": "32688370560444",
                    "SendMonitor": {
                        "Start": "2023-03-30T21:31:19.44Z",
                        "Bytes": "276399460",
                        "Samples": "118930",
                        "InstRate": "3815",
                        "CurRate": "3580",
                        "AvgRate": "8456",
                        "PeakRate": "1340470",
                        "BytesRem": "0",
                        "Duration": "32688380000000",
                        "Idle": "200000000",
                        "TimeRem": "0",
                        "Progress": 0,
                        "Active": true
                    },
                    "RecvMonitor": {
                        "Start": "2023-03-30T21:31:19.44Z",
                        "Bytes": "426940179",
                        "Samples": "127727",
                        "InstRate": "9688",
                        "CurRate": "18331",
                        "AvgRate": "13061",
                        "PeakRate": "1324680",
                        "BytesRem": "0",
                        "Duration": "32688380000000",
                        "Idle": "160000000",
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
                            "RecentlySent": "41212"
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
                            "RecentlySent": "788"
                        },
                        {
                            "ID": 33,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "10",
                            "RecentlySent": "29106"
                        },
                        {
                            "ID": 34,
                            "SendQueueCapacity": "100",
                            "SendQueueSize": "0",
                            "Priority": "7",
                            "RecentlySent": "3710"
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
                "remote_ip": "34.194.74.157"
            }
        ]
    }
}
```
{% endcode %}
