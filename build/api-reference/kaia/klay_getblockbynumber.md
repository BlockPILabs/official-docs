---
description: >-
  Returns information about a block by block number. This API works only on RPC
  call, not on JavaScript console.
---

# klay\_getBlockByNumber

#### **Parameters**

| Type            | Description                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------- |
| QUANTITY \| TAG | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`         |
| Boolean         | If `true` it returns the full transaction objects, if `false` only the hashes of the transactions. |

#### **Return Value**

See [Klaytn Docs](https://docs.klaytn.foundation/dapp/json-rpc/api-references/klay/block#klay_getheaderbyhash)

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getBlockByNumber","params":["0x1b4", true],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":1,
  "result":{
    "baseFeePerGas":"0x0",
    "blockscore":"0x1",
    "extraData":"0xda83010800846b6c617989676f312e31362e31338664617277696e0000000000f89ed5949712f943b296758aaae79944ec975884188d3a96b841ddfdf7e2cb0a93538f757f87f23a93ee35df703c781c6f15e31e4978ecdfb3501fc00924372b9a01df2bc452f2a924c242d83580183d131c47e49a25b78f625201f843b841b9b6034d5a8c5f5b057274cda4f427614cd1f448ee781f4c4322861d1361d09d47d6030f2b69a26cb426db984f54e71f8c112fbf882930ccd715d595e8d8307500",
    "gasUsed":"0x0",
    "governanceData":"0x",
    "hash":"0xe882d7a16f38126dc0c507f990b3fe18fa2d3a380002538581327abe96ca6edc",
    "logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "number":"0x1e67",
    "parentHash":"0x28b1c054346c3bd083741c757a750dcabf94b6d50c7f87158753544e96e73550",
    "receiptsRoot":"0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
    "reward":"0x4b2c736fd05c2e2da3ccbd001a395a444f16a861",
    "size":"0x272",
    "stateRoot":"0xdf9885621c9e6e75912ca94d6987bcb1b54fef0e4a99cbec5e68f1ffc7468a78",
    "timestamp":"0x62130beb",
    "timestampFoS":"0x0",
    "totalBlockScore":"0x1e68",
    "transactions":[],
    "transactionsRoot":"0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
    "voteData":"0x"
  }
}
```
{% endcode %}
