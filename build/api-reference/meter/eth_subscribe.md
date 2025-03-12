---
description: >-
  Subscribe to different Ethereum event types like newHeads, logs,
  pendingTransactions, and minedTransactions using WebSockets.
---

# eth\_subscribe

#### **Parameters:**

* **Event types**- specifies the type of event to listen to (ex: new pending transactions, logs, etc.)
* **Optional params** - optional parameters to include to describe the type of event to listen to (ex: `address`)

#### **Returns:**

While the subscription is active, you will receive events formatted as an object described below:

* Event Object:
  * `jsonrpc`: Always "2.0"
  * `method`: Always "eth\_subscription"
  * `params`: An object with the following fields:
    * `subscription`: The subscription ID returned by the `eth_subscribe` call which created this subscription. This ID will be attached to all received events and can also be used to cancel the subscription using `eth_unsubscribe`
    * `result`: An object whose contents vary depending on the event type.

#### Example:

{% code overflow="wrap" %}
```json
// initiate websocket stream 
wscat -c wss://meter.blockpi.network/v1/ws/<your-api-key>

//create an event
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["newHeads"]}

// Result
{"jsonrpc":"2.0","method":"eth_subscription","params":{"subscription":"0xa1ac5d4c9fcea839f584351871d6c7ed","result":{"parentHash":"0xa9e8a30da9a6d50dde5fa12a576d277185d67a676c7dccd185faf9e11d1e188e","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","miner":"0x690b9a9e9aa1c9db991c7721a92d351db4fac990","stateRoot":"0x636d352775b2cac96da16e2280c1582b41d211c2c30fe3b6e28de2f931ee09fd","transactionsRoot":"0x6bee70c75c2dce89e6dd676072370f73e7ca48a00dbde15fe3eaa2d6272f33eb","receiptsRoot":"0xcc98d1e6ae8c0fe998087fe2da57dc9dbf094a7926ed0081653f7f96bef00629","logsBloom":"0xd2f959bc2759dbaef7bd1119c6b5d3b58dd6a6259e0e81ed70592256ff98b5ffad640740f1a5255c5b4b9a497ee8ff88472582aebb57fbe42ecccbd752ff61e16049d9904ff5cf4eea72f2fc5dfa4ef1978330fd7e4d9f62f9856f65cd6efc33834e996c3727c65662c6dbe13c73e8fdaefaf0719c3d9e511455d23fafaea5b40ac5bf77aaeb77545749ae6c10a2a7a9f4f2ddaded68dd3e5be8e5e8c11b1624dffe7fe7cd866e935a97f9dc3f5bccd857e5c027e12af27a2bf346b59088a05f45f82033e3ccb181e78ddf1593aa765e55613c66dcafafba57463a1bbb3df0627f3bbdf8c8ddaddc148ed7846de7832c171adb61595e99ec7951bec2b7037e12","difficulty":"0x0","number":"0xfe04bf","gasLimit":"0x1c9c380","gasUsed":"0x11edb89","timestamp":"0x63ef3fc3","extraData":"0x6275696c64657230783639","mixHash":"0x8ceef9ce28d1e6e2197b4308ee2539fdbb50f669a4ef03b04276dd71ea95ccd7","nonce":"0x0000000000000000","baseFeePerGas":"0x4edaf85fd","hash":"0xf17bf048feb50e444ea144a649da51629e3119f814cd906eda76180e75778680"}}}
```
{% endcode %}
