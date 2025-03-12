---
description: Returns an array of all logs matching a given filter object.
---

# klay\_getLogs

The execution of this API can be limited by two node configurations to manage resources of Klaytn node safely.

#### **Parameters**

`Object` - The filter options:

| Name      | Type                  | Description                                                                                                                                                                                                                                                                                                      |
| --------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fromBlock | QUANTITY \| TAG       | (optional, default: `"latest"`) Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`                                                                                                                                                                                       |
| toBlock   | QUANTITY \| TAG       | (optional, default: `"latest"`) Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`                                                                                                                                                                                       |
| address   | 20-byte DATA \| Array | (optional) Contract address or a list of addresses from which logs should originate.                                                                                                                                                                                                                             |
| topics    | Array of DATA         | (optional) Array of 32-byte DATA topics. Topics are order-dependent. Each topic can also be an array of DATA with “or” options.                                                                                                                                                                                  |
| blockHash | 32-byte DATA          | (optional) A filter option that restricts the logs returned to the single block with the 32-byte hash blockHash. Using blockHash is equivalent to fromBlock = toBlock = the block number with hash blockHash. If blockHash is present in in the filter criteria, then neither fromBlock nor toBlock are allowed. |

{% hint style="info" %}
The block range of klay\_getLogs is limited to 1024. Requests with blocks over this range will get an error.
{% endhint %}

#### **Return Value**

See [klay\_getFilterChanges](broken-reference)

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getLogs","params":[{"fromBlock":"0x1","toBlock":"latest","address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b"}],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":1,
  "result":[
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xfa9b2165fc71c1d6ffa03291c7f5d223ea363ec063d747eec9ce2d30d24855ef"],
      "data":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000060000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b481000000000000000000000000000000000000000000000000000000000000001341646472657373426f6f6b436f6e747261637400000000000000000000000000",
      "blockNumber":"0xd3b5",
      "transactionHash":"0x57ca8ff0a0d454d4c5418694c21bc4ef3de26cf7cd18dd404d6a7189a826bfe0",
      "transactionIndex":"0x0",
      "blockHash":"0x279251a907c6ab1fb723595511ff401432e7c2437d54189298f53a7d33ce3a60",
      "logIndex":"0x0",
      "removed":false
    },
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xfa3e1e272694072320aad73a3fadd8876c4bf8f40899c6c7ce2fda9f4e652cfa"],
      "data":"0x00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000000300000000000000000000000041383b6ee0ea5108d6b139165a9c85351aacd39800000000000000000000000057f7439898e652fa9b5654022297588532e5e0370000000000000000000000005b5b7a718a4124eb746ae00b1ce6edcaa5ab55bc",
      "blockNumber":"0xd3b5",
      "transactionHash":"0x57ca8ff0a0d454d4c5418694c21bc4ef3de26cf7cd18dd404d6a7189a826bfe0",
      "transactionIndex":"0x0",
      "blockHash":"0x279251a907c6ab1fb723595511ff401432e7c2437d54189298f53a7d33ce3a60",
      "logIndex":"0x1",
      "removed":false
    },
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"],
      "data":"0x000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b481000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000003000000000000000000000000286d09b578d6126e09296dfe6c775ea7d0cf06e9000000000000000000000000860350f6d774efd16046335c388b832b910d3f8c00000000000000000000000061a7cbdd597848494fa85cbb76f9c63ad9c06cad",
      "blockNumber":"0x14d96",
      "transactionHash":"0x73282602d2f908180f47e3c8673f41c0899cbbb2d606976c2f77188ffa57d6e7",
      "transactionIndex":"0x0",
      "blockHash":"0xa5268a093cd5df7eccde18217a7019a35ab761088312027af16682aafa704ee3",
      "logIndex":"0x1",
      "removed":false
    },
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"],
      "data":"0x000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b4810000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000030000000000000000000000002f91d1b79dd06da1b622122d61e05e64562de61e0000000000000000000000006e76e0ce76dfba55060400144318d4821a58510600000000000000000000000031b93ca83b5ad17582e886c400667c6f698b8ccd",
      "blockNumber":"0x14e4e",
      "transactionHash":"0xf9d86ed451d67abc68c517f7fa0e0a7a8e3dedec23f56febda2b7f52d35185b6",
      "transactionIndex":"0x0",
      "blockHash":"0x7ddf4a0a203d40afc1706aa24b787da601e1bce326319349d0eeef6c41656fa5",
      "logIndex":"0x1",
      "removed":false
    }
  ]
}
```
{% endcode %}

{% code overflow="wrap" %}
```json
// Request
$ curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getLogs","params":[{"fromBlock":"earliest","toBlock":"latest","topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"]}],"id":2}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":2,
  "result":[
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"],
      "data":"0x000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b481000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000003000000000000000000000000286d09b578d6126e09296dfe6c775ea7d0cf06e9000000000000000000000000860350f6d774efd16046335c388b832b910d3f8c00000000000000000000000061a7cbdd597848494fa85cbb76f9c63ad9c06cad",
      "blockNumber":"0x14d96",
      "transactionHash":"0x73282602d2f908180f47e3c8673f41c0899cbbb2d606976c2f77188ffa57d6e7",
      "transactionIndex":"0x0",
      "blockHash":"0xa5268a093cd5df7eccde18217a7019a35ab761088312027af16682aafa704ee3",
      "logIndex":"0x1",
      "removed":false
    },
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"],
      "data":"0x000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b4810000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000030000000000000000000000002f91d1b79dd06da1b622122d61e05e64562de61e0000000000000000000000006e76e0ce76dfba55060400144318d4821a58510600000000000000000000000031b93ca83b5ad17582e886c400667c6f698b8ccd",
      "blockNumber":"0x14e4e",
      "transactionHash":"0xf9d86ed451d67abc68c517f7fa0e0a7a8e3dedec23f56febda2b7f52d35185b6",
      "transactionIndex":"0x0",
      "blockHash":"0x7ddf4a0a203d40afc1706aa24b787da601e1bce326319349d0eeef6c41656fa5",
      "logIndex":"0x1",
      "removed":false
    },
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"],
      "data":"0x000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b481000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000003000000000000000000000000a2b1264624c92257dd8e7f0cac42d451061d1510000000000000000000000000b381ee81e319e5ec48f42d0b47b5e4361c9a6f740000000000000000000000003855407fa65c4c5104648b3a9e495072df62b585",
      "blockNumber":"0x14f38",
      "transactionHash":"0xc8f8c637ea9fcbe71e23fe0779b59fb10173e8c4fd7e49bce3cce76ff67d353d",
      "transactionIndex":"0x0",
      "blockHash":"0xb1717038e443f517bd7a8c37b66fb731fed573f5fa5486ebbbb5e4c9060be50b",
      "logIndex":"0x1",
      "removed":false
    },
    {
      "address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b",
      "topics":["0xc7b359b1e189b7d721be7f0765a8d745be718566b8e67cbd2728dae5d6fd64b6"],
      "data":"0x000000000000000000000000d3564e57bb5c6f4d983a493a946534f8e1e8b4810000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000030000000000000000000000009dd579f23912665b956b0cd50387b29a62052732000000000000000000000000c98a86af2eca2989c0cb2a2b8d4bb841f11e94ab000000000000000000000000f65e07b6626ab43ecea744803fa46bd4a89bfdb6",
      "blockNumber":"0x14fe7",
      "transactionHash":"0x14da1883bb2aae487ce1cb93cd39bc9bb802adbba083f337051877358150ab3f",
      "transactionIndex":"0x0",
      "blockHash":"0xcd820189f00e9a6faaea7313437b92114e69bd32e18b4a28e7763117716c6fa9",
      "logIndex":"0x1",
      "removed":false
    }
  ]
}
```
{% endcode %}
