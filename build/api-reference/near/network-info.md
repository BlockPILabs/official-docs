---
description: >-
  Returns the current state of node network connections (active peers,
  transmitted data, etc.)
---

# Network Info

* method: `network_info`
* params: _none_

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "network_info",
  "params": []
}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "active_peers": [
      {
        "id": "ed25519:GkDv7nSMS3xcqA45cpMvFmfV1o4fRF6zYo1JRR6mNqg5",
        "addr": "35.193.24.121:24567",
        "account_id": null
      }
    ],
    "num_active_peers": 34,
    "peer_max_count": 40,
    "sent_bytes_per_sec": 17754754,
    "received_bytes_per_sec": 492116,
    "known_producers": [
      {
        "account_id": "node0",
        "addr": null,
        "peer_id": "ed25519:7PGseFbWxvYVgZ89K1uTJKYoKetWs7BJtbyXDzfbAcqX"
      }
    ]
  },
  "id": "dontcare"
}
```
{% endcode %}
