---
description: Returns bytecode of a transaction given by its hash.
---

# zks\_getBytecodeByHash

#### **Parameters:**

**hash-H256**, Hash address as string.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getBytecodeByHash", "params": [ "0x0100067d861e2f5717a12c3e869cfb657793b86bbb0caa05cc1421f16c5217bc" ]}'

// Result
{
    "jsonrpc": "2.0",
    "result": [
        0,
        4,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        11,
        ...,
        ...,
            ],
    "id": 1
}



```
{% endcode %}
