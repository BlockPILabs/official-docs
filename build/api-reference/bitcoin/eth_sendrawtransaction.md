---
description: >-
  Return information about all known tips in the block tree, including the main
  chain as well as orphaned branches.
---

# getchaintips

#### **Parameters:**

**None**

#### **Returns:**

```
[                        (json array)
  {                      (json object)
    "height" : n,        (numeric) height of the chain tip
    "hash" : "hex",      (string) block hash of the tip
    "branchlen" : n,     (numeric) zero for main chain, otherwise length of branch connecting the tip to the main chain
    "status" : "str"     (string) status of the chain, "active" for the main chain
                         Possible values for status:
                         1.  "invalid"               This branch contains at least one invalid block
                         2.  "headers-only"          Not all blocks for this branch are available, but the headers are valid
                         3.  "valid-headers"         All blocks are available for this branch, but they were never fully validated
                         4.  "valid-fork"            This branch is not part of the active chain, but is fully validated
                         5.  "active"                This is the tip of the active main chain, which is certainly valid
  },
  ...
]
```

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bitcoin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc": "1.0", "id": "1", "method": "getchaintips", "params": [ ]}'

// Result
{
    "result": [
        {
            "height": 910820,
            "hash": "0000000000000000000134891ac230d7056bb6de1e2b980241da747e070d97c1",
            "branchlen": 0,
            "status": "active"
        },
        {
            "height": 907051,
            "hash": "00000000000000000001aad53cc3e15fcf36766a25b15ac8c6d84fe2c2055e82",
            "branchlen": 1,
            "status": "valid-headers"
        }
    ],
    "error": null,
    "id": "1"
}
```
{% endcode %}
