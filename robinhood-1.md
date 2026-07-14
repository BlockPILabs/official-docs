# robinhood

> Robinhood is an Arbitrum Orbit L3 chain (Chain ID: 4663 / 0x1237). It is fully EVM-compatible and runs on the Nitro execution client.

BlockPI supports the following JSON-RPC methods for the Robinhood network. All requests should be made to:

```bash
https://robinhood.blockpi.network/v1/rpc/your-rpc-key
```

{% hint style="info" %}
The block range of `eth_getLogs` is limited to **1024** for public endpoints and **5000** for private endpoints. Requests with blocks over this range will get an error.
{% endhint %}

## eth

* [eth\_chainId](/broken/pages/34c9c8e4bb1daa60b26ca3e7420f0ff45cec885a)
* [eth\_syncing](/broken/pages/34224f57398278579e4b80e80c90f5d12f484fd1)
* [eth\_blockNumber](/broken/pages/2a91dc168b1a10e7bf43c7bf59bc16cd31ccbce4)
* [eth\_gasPrice](/broken/pages/a43e43972a2cb9c4653e1f57e956c3c2228f2334)
* [eth\_getBalance](/broken/pages/761096190d618e5bea287df71c25119366a16dd3)
* [eth\_getBlockByNumber](/broken/pages/9c9970eaa61a30eb7c6c6bfd5c80c59ab6df35d5)
* [eth\_getBlockByHash](/broken/pages/ae1b9888a83ac546aad74ebb45a2fa25866ef54a)
* [eth\_getBlockReceipts](/broken/pages/8f2ed184f947b791633e8244189c94e00ee8ad01)
* [eth\_sendRawTransaction](/broken/pages/7779178f0de5dde59bfde048d0ca3ef339a27475)
* [eth\_getTransactionByHash](/broken/pages/0a410e4fa105af200608abe7ed2eaf6fa0152ab5)
* [eth\_getTransactionByBlockNumberAndIndex](/broken/pages/6d004cbe8463f24f7c8008365e86dc6db8695464)
* [eth\_getTransactionByBlockHashAndIndex](/broken/pages/ce0cbf779b4ed6b1270b7f1439df1d5a14bbffec)
* [eth\_getTransactionCount](/broken/pages/c16de99a5254f61ed1e319575f2f4b3aed530875)
* [eth\_getTransactionReceipt](/broken/pages/187e792e17bc62853cc867e5f6068c6ffac3fabc)
* [eth\_getBlockTransactionCountByNumber](/broken/pages/6061f784a7c688b70083330d46e8594a9538acb5)
* [eth\_getBlockTransactionCountByHash](/broken/pages/bad95f1e4b2de0f05cf29a084ecce4e2a061512f)
* [eth\_getLogs](/broken/pages/b85ab92ba023ca225871de161faf578cd2d2593e)
* [eth\_getCode](/broken/pages/0b340afa7250c821c5cc5b5b5b8aeea13d2e3a4b)
* [eth\_call](/broken/pages/41549c9c9847bb999c93cc19a5db98dbf6bfea1e)
* [eth\_getStorageAt](/broken/pages/1272af0904c49b0ad78f841057e050b88b7087f9)
* [eth\_estimateGas](/broken/pages/3a6d291c40b9873465d9d43a6b2fb000c3f3fad2)
* [eth\_newFilter](/broken/pages/5895559b42d293e3b9353aba8b6aee526d651a80)
* [eth\_newBlockFilter](/broken/pages/15a1acf11ee65609127beaed7a92d6024b5aa166)
* [eth\_newPendingTransactionFilter](/broken/pages/5d4874d6e0452a9e15db5327f32ad1a9df94e401)
* [eth\_getFilterChanges](/broken/pages/aa717de575a67f0a397201b6b0664882da052a4e)
* [eth\_uninstallFilter](/broken/pages/7685d25c15dd6fd3692b4ce5f9fb0159ccbef679)

## net

* [net\_version](/broken/pages/abac78edceeaba1a534c8f3ed1d12a3df8995a96)

## web3

* [web3\_clientVersion](/broken/pages/4b9ac20fcc7bfeff608245b2fb3d64581ba5baab)
* [web3\_sha3](/broken/pages/fd90989e98f4b021f5337670cc3a6a772e497ca1)
