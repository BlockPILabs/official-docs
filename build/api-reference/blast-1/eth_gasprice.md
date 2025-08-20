# getblockheader

If verbose is false, returns a string that is serialized, hex-encoded data for blockheader ‘hash’.

If verbose is true, returns an Object with information about blockheader ‘hash’.

#### **Parameters:**

string, required. The block hash

boolean, optional, default=true. true for a json object, false for the hex-encoded data

#### **Returns:**

#### for verbose = true

```
{                                 (json object)
  "hash" : "hex",                 (string) the block hash (same as provided)
  "confirmations" : n,            (numeric) The number of confirmations, or -1 if the block is not on the main chain
  "height" : n,                   (numeric) The block height or index
  "version" : n,                  (numeric) The block version
  "versionHex" : "hex",           (string) The block version formatted in hexadecimal
  "merkleroot" : "hex",           (string) The merkle root
  "time" : xxx,                   (numeric) The block time expressed in UNIX epoch time
  "mediantime" : xxx,             (numeric) The median block time expressed in UNIX epoch time
  "nonce" : n,                    (numeric) The nonce
  "bits" : "hex",                 (string) The bits
  "difficulty" : n,               (numeric) The difficulty
  "chainwork" : "hex",            (string) Expected number of hashes required to produce the current chain
  "nTx" : n,                      (numeric) The number of transactions in the block
  "previousblockhash" : "hex",    (string) The hash of the previous block
  "nextblockhash" : "hex"         (string) The hash of the next block
}
```

### for verbose=false

string, A string that is serialized, hex-encoded data for block ‘hash’

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getblockheader", "params": ["000000000000000000020b1823dfd1bd92b9ae7821a38e63ac24e06db765d7db"]}'

// Result
{
    "result": {
        "hash": "000000000000000000020b1823dfd1bd92b9ae7821a38e63ac24e06db765d7db",
        "confirmations": 2,
        "height": 910819,
        "version": 715235328,
        "versionHex": "2aa1a000",
        "merkleroot": "276aaed67b964f1f83216b137d38f9bf40b878f05aa372b50771bf9d54030290",
        "time": 1755652254,
        "mediantime": 1755650531,
        "nonce": 2523797606,
        "bits": "17022cb3",
        "target": "000000000000000000022cb30000000000000000000000000000000000000000",
        "difficulty": 129435235580344.8,
        "chainwork": "0000000000000000000000000000000000000000db8e5b70b171b2f326098cdc",
        "nTx": 5039,
        "previousblockhash": "00000000000000000001b33d05fa5fee574c4f97832e1840ce676702d72aafda",
        "nextblockhash": "0000000000000000000134891ac230d7056bb6de1e2b980241da747e070d97c1"
    },
    "error": null,
    "id": "1"
}
```
{% endcode %}
