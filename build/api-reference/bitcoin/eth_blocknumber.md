---
description: Returns hash of block in best-block-chain at height provided.
---

# getblockhash

#### **Parameters:**

&#x20;numeric, required. The height index

string, optional, default=basic. The type name of the filter

#### **Returns:**

```
{                      (json object)
  "filter" : "hex",    (string) the hex-encoded filter data
  "header" : "hex"     (string) the hex-encoded filter header
}
```

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getblockhash", "params": [1000]}'

// Result
{
    "result": "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09",
    "error": null,
    "id": "1"
}
```
{% endcode %}
