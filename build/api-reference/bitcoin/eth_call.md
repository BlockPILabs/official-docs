---
description: Returns statistics about the unspent transaction output set.
---

# gettxoutsetinfo

#### **Parameters:**

string, optional, default=hash\_serialized\_2. Which UTXO set hash should be calculated. Options: ‘hash\_serialized\_2’ (the legacy algorithm), ‘none’.

#### **Returns:**

```
{                                 (json object)
  "height" : n,                   (numeric) The current block height (index)
  "bestblock" : "hex",            (string) The hash of the block at the tip of the chain
  "transactions" : n,             (numeric) The number of transactions with unspent outputs
  "txouts" : n,                   (numeric) The number of unspent transaction outputs
  "bogosize" : n,                 (numeric) A meaningless metric for UTXO set size
  "hash_serialized_2" : "hex",    (string) The serialized hash (only present if 'hash_serialized_2' hash_type is chosen)
  "disk_size" : n,                (numeric) The estimated size of the chainstate on disk
  "total_amount" : n              (numeric) The total amount
}
```

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"gettxoutsetinfo","params":[ ],"id":1}'

// Result

```
{% endcode %}
