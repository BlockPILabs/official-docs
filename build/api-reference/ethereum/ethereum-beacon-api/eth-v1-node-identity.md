---
description: Retrieves data about the node's network presence
---

# /eth/v1/node/identity



#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/node/identity

// Result
{
    "data": {
        "peer_id": "16Uiu2HAkxLCknuVd9mhH3aA3PzqcBnVg3RqSPE1j4riKfyu31atm",
        "enr": "enr:-Ma4QJOtYEIvC3syRgRk9ii2yxCn5shXe6n5CWnbc0I8lqvgfcmyuA8q0dUACI9SSl1jgXjGqTecx8EjffDQG6khAPWCAm-HYXR0bmV0c4gAAAAAAAAMAIRldGgykGqVoakEAAAA__________-CaWSCdjSCaXCEojdkeYRxdWljgnpOiXNlY3AyNTZrMaECKyxf0LsV1cQMNwVlSYgE77Nz4P8akrY9Dd5_n46sQP6Ic3luY25ldHMAg3RjcIJ6TYN1ZHCCek0",
        "p2p_addresses": [
            "/ip4/162.55.100.121/tcp/31309/p2p/16Uiu2HAkxLCknuVd9mhH3aA3PzqcBnVg3RqSPE1j4riKfyu31atm"
        ],
        "discovery_addresses": [
            "/ip4/162.55.100.121/udp/31309/p2p/16Uiu2HAkxLCknuVd9mhH3aA3PzqcBnVg3RqSPE1j4riKfyu31atm"
        ],
        "metadata": {
            "seq_number": "587",
            "attnets": "0x0000000000000c00",
            "syncnets": "0x00"
        }
    }
}
```
{% endcode %}
