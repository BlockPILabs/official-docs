---
description: Returns details about an unspent transaction output.
---

# gettxout

#### **Parameters:**

string, required. The transaction id

numeric, required. vout number

boolean, optional, default=true. Whether to include the mempool. Note that an unspent output that is spent in the mempool won’t appear.

#### **Returns:**

```
{                             (json object)
  "bestblock" : "hex",        (string) The hash of the block at the tip of the chain
  "confirmations" : n,        (numeric) The number of confirmations
  "value" : n,                (numeric) The transaction value in BTC
  "scriptPubKey" : {          (json object)
    "asm" : "hex",            (string)
    "hex" : "hex",            (string)
    "reqSigs" : n,            (numeric) Number of required signatures
    "type" : "hex",           (string) The type, eg pubkeyhash
    "addresses" : [           (json array) array of bitcoin addresses
      "str",                  (string) bitcoin address
      ...
    ]
  },
  "coinbase" : true|false     (boolean) Coinbase or not
}
```

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "curltest", "method": "gettxout", "params": ["000000000000000000020b1823dfd1bd92b9ae7821a38e63ac24e06db765d7db", 1]}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": [...]
}
```
{% endcode %}
