---
description: Retrieve details of the chain's genesis which can be used to identify chain.
---

# /eth/v1/beacon/genesis

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/genesis

// Result
{
    "data": {
        "genesis_time": "1606824023",
        "genesis_validators_root": "0x4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95",
        "genesis_fork_version": "0x00000000"
    }
}
```
{% endcode %}
