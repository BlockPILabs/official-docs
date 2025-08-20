---
description: Returns the information about a transaction requested by transaction hash.
---

# getchaintxstats

#### **Parameters:**

numeric, optional, default=one month. Size of the window in number of blocks

string, optional, default=chain tip. The hash of the block that ends the window.

#### **Returns:**

```
{                                       (json object)
  "time" : xxx,                         (numeric) The timestamp for the final block in the window, expressed in UNIX epoch time
  "txcount" : n,                        (numeric) The total number of transactions in the chain up to that point
  "window_final_block_hash" : "hex",    (string) The hash of the final block in the window
  "window_final_block_height" : n,      (numeric) The height of the final block in the window.
  "window_block_count" : n,             (numeric) Size of the window in number of blocks
  "window_tx_count" : n,                (numeric) The number of transactions in the window. Only returned if "window_block_count" is > 0
  "window_interval" : n,                (numeric) The elapsed time in the window in seconds. Only returned if "window_block_count" is > 0
  "txrate" : n                          (numeric) The average rate of transactions per second in the window. Only returned if "window_interval" is > 0
}
```

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getchaintxstats", "params": [ ]}'

// Result
{
    "result": {
        "time": 1755654465,
        "txcount": 1229071016,
        "window_final_block_hash": "000000000000000000008384a549b60549889ea038a2fddc5b752106625c9e98",
        "window_final_block_height": 910821,
        "window_block_count": 4320,
        "window_interval": 2562996,
        "window_tx_count": 12784026,
        "txrate": 4.987922727932466
    },
    "error": null,
    "id": "1"
}
```
{% endcode %}
