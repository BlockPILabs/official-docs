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
wscat -c wss://oasys.blockpi.network/v1/ws/<your-api-key>

//create an event
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["newHeads"]}

// Result
{"jsonrpc":"2.0","id":2,"result":"0x55b8d6707eff7d91de9d1a1e566adf83"}
{"jsonrpc":"2.0","method":"eth_subscription","params":{"subscription":"0x55b8d6707eff7d91de9d1a1e566adf83","result":{"parentHash":"0x9895467d6859c1d244dd48cdfe3ea9944af8446af80176c0be20279b153e9519","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","miner":"0x9d1abbdd9acd80f6e8ac087e8cfd5a6b2b1c4043","stateRoot":"0x0330151e9284920d7cc9d370d775f802fc1c16f1de2b236b243ec0d67f23f574","transactionsRoot":"0x8025c81ca1f759406203177003d509efe9f35540dde5cc2ba0363dcf2e49c863","receiptsRoot":"0x62e1327e4d9ae7c4c57ebb35e4a991065633f9fd289fa34ca34b61b51d5aabfd","logsBloom":"0x00000000000000000000000000000000000000002040000000000000000000000000000000000000000000004000000000000000000000000000000000040000000040000000000202000000000000000000000000000000000000800000000000008010000000000000000000000000000000000010002000000000000000000000000000000000010008000000000000000000000000000000000000000200000000000000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000080000000000004000000000000080000000002000000000000000000000000000000000000000","difficulty":"0x2","number":"0xfecaf","gasLimit":"0x1c9c380","gasUsed":"0x45f83","timestamp":"0x6424eda9","extraData":"0xd883010005846765746888676f312e31372e38856c696e757800000000000000f2b2867c45e4d7a8ccfd640cf05dc4153865771db3c43e7f37864cc39a5e7ce44bef9b9c4b8bdb933293526150987536b0f764c7accd8a57074e04cd90b4f3a700","mixHash":"0x0000000000000000000000000000000000000000000000000000000000000000","nonce":"0x0000000000000000","baseFeePerGas":"0x7","hash":"0x9571eeb375f4599854a348a4a6a5bf930f110108f558dce56254a967eca05da3"}}}
```
{% endcode %}
