---
description: Returns mempool data for given transaction
---

# getmempoolinfo

#### **Parameters:**

None

#### **Returns:**

```
{                            (json object)
  "loaded" : true|false,     (boolean) True if the mempool is fully loaded
  "size" : n,                (numeric) Current tx count
  "bytes" : n,               (numeric) Sum of all virtual transaction sizes as defined in BIP 141. Differs from actual serialized size because witness data is discounted
  "usage" : n,               (numeric) Total memory usage for the mempool
  "maxmempool" : n,          (numeric) Maximum memory usage for the mempool
  "mempoolminfee" : n,       (numeric) Minimum fee rate in BTC/kB for tx to be accepted. Is the maximum of minrelaytxfee and minimum mempool fee
  "minrelaytxfee" : n,       (numeric) Current minimum relay fee for transactions
  "unbroadcastcount" : n     (numeric) Current number of transactions that haven't passed initial broadcast yet
}
```

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getmempoolinfo", "params": [ ]}'

// Result
{
    "result": {
        "loaded": true,
        "size": 3279,
        "bytes": 1511095,
        "usage": 8355680,
        "total_fee": 0.03419250,
        "maxmempool": 300000000,
        "mempoolminfee": 0.00001000,
        "minrelaytxfee": 0.00001000,
        "incrementalrelayfee": 0.00001000,
        "unbroadcastcount": 0,
        "fullrbf": true
    },
    "error": null,
    "id": "1"
}
```
{% endcode %}
