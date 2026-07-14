# Robinhood

> Robinhood is an Arbitrum Orbit L3 chain (Chain ID: 4663 / 0x1237). It is fully EVM-compatible and runs on the Nitro execution client.

BlockPI supports the following JSON-RPC methods for the Robinhood network. All requests should be made to:

```
https://robinhood.blockpi.network/v1/rpc/your-rpc-key
```

{% hint style="info" %}
The block range of `eth_getLogs` is limited to **1024** for public endpoints and **5000** for private endpoints. Requests with blocks over this range will get an error.
{% endhint %}

## eth

* [eth\_chainId](/broken/pages/8efcf70845686a2787f5eba0d4658c9619fcb452)
* [eth\_syncing](/broken/pages/825ab33ff4e30fc8117f565da331a33f1f2e80d6)
* [eth\_blockNumber](/broken/pages/3f5ebf41a3f8b3dbc5f99a6b0dbc87f84157e6d2)
* [eth\_gasPrice](/broken/pages/3f3dc7e3143ac03dab91e14c9934eb88c3c66f11)
* [eth\_getBalance](/broken/pages/66279c05496e0c14770b1e77d57bf17e508acfeb)
* [eth\_getBlockByNumber](/broken/pages/0b4c88457ac5f4686c553f645e1e3c59b16c7e1a)
* [eth\_getBlockByHash](/broken/pages/e1e730900f185f151c034cf6e94e89fdbd2ecd9e)
* [eth\_getBlockReceipts](/broken/pages/db0a4694e8b6c5a99e475a548cbbdcb81b99bdbf)
* [eth\_sendRawTransaction](/broken/pages/6c3c88eab867716ee9fb34d5b7f6b554e202ea0c)
* [eth\_getTransactionByHash](/broken/pages/afe30d0cab7d52d4df403c232fa80ac7a64f2359)
* [eth\_getTransactionByBlockHashAndIndex](/broken/pages/1f335ce9512ed0888868a59dab6a02d045809edc)
* [eth\_getTransactionByBlockNumberAndIndex](/broken/pages/b01cdbf0a0d7404b6aaeb33fd0feab830bf5f750)
* [eth\_getTransactionReceipt](/broken/pages/df28767666c7f04e8bdefe06ba5b571ca2512e01)
* [eth\_getTransactionCount](/broken/pages/ced68cb5f3e6d98878a6e40e94cb5310e03026f7)
* [eth\_getBlockTransactionCountByNumber](/broken/pages/e9559b0074c02bc277c79b2e753ef15e63e6e317)
* [eth\_getBlockTransactionCountByHash](/broken/pages/32cfae295ef56e47f557e5d40f4b4fe9e633a24e)
* [eth\_getLogs](/broken/pages/4b9f6a8373f1e23e6531990ba2c6da541e9138ea)
* [eth\_getCode](/broken/pages/2b5993681792d9fc39599dbf8ae5e34662266633)
* [eth\_call](/broken/pages/f1d1df27eb4d9e698cd7e0b560e9460f906ad3a4)
* [eth\_getStorageAt](/broken/pages/0051bf877d3199936984d756ad4ecd04e1b251c5)
* [eth\_estimateGas](/broken/pages/d89ed047b991c5218da97b22861ff506897dfcf3)
* [eth\_newFilter](/broken/pages/a0609c3dd5489e6121a53fb4ecc40c92aa1788f5)
* [eth\_newBlockFilter](/broken/pages/b3cd20f120cbbd4e33c8776758ab4882f5200a6a)
* [eth\_newPendingTransactionFilter](/broken/pages/85b6be23717a8dffd51a0b3eee9e7b59bafab577)
* [eth\_getFilterChanges](/broken/pages/dd50c8f833bad6eba286c80eeb7f1848f78bb96f)
* [eth\_uninstallFilter](/broken/pages/0d18315753c01f6f8e0705c28be1eb2ff5ce0b48)

## net

* [net\_version](/broken/pages/89f05f59d62ba10d5cf2ba245c701443a75758c6)

## web3

* [web3\_clientVersion](/broken/pages/49117c5f48514547f018f34da2e7c0e4f0905373)
* [web3\_sha3](/broken/pages/c705f4f8c1ddce14a10f09ed58f37d11cdcf30d7)
