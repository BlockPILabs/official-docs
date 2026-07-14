# robinhood

> Robinhood is an Arbitrum Orbit L3 chain (Chain ID: 4663 / 0x1237). It is fully EVM-compatible and runs on the Nitro execution client.

BlockPI supports the following JSON-RPC methods for the Robinhood network. All requests should be made to:

```
https://robinhood.blockpi.network/v1/rpc/your-rpc-key
```

{% hint style="info" %}
The block range of `eth_getLogs` is limited to **1024** for public endpoints and **5000** for private endpoints. Requests with blocks over this range will get an error.
{% endhint %}

## eth

* [eth\_chainId](/broken/pages/e1ff79fb026e2780f3d3d0c28af48a01f4551bd1)
* [eth\_syncing](/broken/pages/6f7d33b9b1d7536745c8bd78c7d1ea1554622e86)
* [eth\_blockNumber](/broken/pages/ca7f86e6d344180d397253f6ebdbeb197e0ca580)
* [eth\_gasPrice](/broken/pages/1320d0fabbdef9ca49cedc053c3bd0b6ee8cb707)
* [eth\_getBalance](/broken/pages/02fa9bd65e62b4ccdcbb95908012081cae7c6037)
* [eth\_getBlockByNumber](/broken/pages/fa484347d7c4e1c50e2523f66ba8a8f038e8d5c7)
* [eth\_getBlockByHash](/broken/pages/049fd69d03e452310c7613de182898651f127239)
* [eth\_getBlockReceipts](/broken/pages/ecd0aa9fadfafae633c3f18dc77a5147679984d2)
* [eth\_sendRawTransaction](/broken/pages/4ccf4ee43ea56a65f1cf2c7c53320980396bf6f1)
* [eth\_getTransactionByHash](/broken/pages/f33d6936176db7c5afe6f0182d924d081f6662a0)
* [eth\_getTransactionByBlockHashAndIndex](/broken/pages/42a1421eaa22ab90eb806f75411c365f0d081153)
* [eth\_getTransactionByBlockNumberAndIndex](/broken/pages/523b8ca29165b3be93054eabc9e55e2c4307488e)
* [eth\_getTransactionReceipt](/broken/pages/6e65e94795aae48de9123462ec507369139d66f5)
* [eth\_getTransactionCount](/broken/pages/cb0f7bd54deddcb9557c31d3b018550dfa355602)
* [eth\_getBlockTransactionCountByNumber](/broken/pages/47157fc13543834baaf96880974cdb5e2668e575)
* [eth\_getBlockTransactionCountByHash](/broken/pages/498284880f186f51da0fc29407716e3cf58230c9)
* [eth\_getLogs](/broken/pages/abda5008f82be796d182f949bf0f3c75726dd449)
* [eth\_getCode](/broken/pages/6480c2f2f7463daa7fbece108e6d49f96507a096)
* [eth\_call](/broken/pages/4b712a5b24062c2a2fc0b1043a9783383c141857)
* [eth\_getStorageAt](/broken/pages/4071d662bd9e70ba49f03829643026cbd3f3ad24)
* [eth\_estimateGas](/broken/pages/0078dddae43cd127920ae2d454df93f03bd81b7e)
* [eth\_newFilter](/broken/pages/df462e2ad3ee0f83e4e351d35fc1858504f2b0c0)
* [eth\_newBlockFilter](/broken/pages/31ffac60723ef330164419d593d8469d1b3c7e2a)
* [eth\_newPendingTransactionFilter](/broken/pages/90c95cf224fe3a5303b7b96aef26710646e37b4e)
* [eth\_getFilterChanges](/broken/pages/2e45213e355ca8790112f8cb2aa1ae45ab9b2889)
* [eth\_uninstallFilter](/broken/pages/4f921663b8a19af7aecfa403a4adfb5b79798e20)

## net

* [net\_version](/broken/pages/01603008b5baa3df3fb376ef14b4b9963b9ed49f)

## web3

* [web3\_clientVersion](/broken/pages/9c99dbaaf8bd615b8a5a64fcfb41d16f60f7329d)
* [web3\_sha3](/broken/pages/6ea36f5059dae4c3ab6a86ff823cbb0b6beb0e09)
