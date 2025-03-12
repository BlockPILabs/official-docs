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
wscat -c wss://cronos.blockpi.network/v1/ws/<your-api-key>

//create an event
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["newHeads"]}

// Result
{"jsonrpc":"2.0","method":"eth_subscription","params":{"subscription":"0x6aa246f04e371c082de2be4832b8dec4","result":{"parentHash":"0xa99ebb1ec60b7a5867bd1d33a4264ec56cd3c774392d1e0be04b069a6591897c","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","miner":"0x1ea0cd8f529d96af6e426450882b12a3b09e0e62","stateRoot":"0xb35828003fd1414c56b3b7f534a351aa71cfde0a816fceef4aae767319126501","transactionsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421","receiptsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421","logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000","difficulty":"0x0","number":"0x6c392e","gasLimit":"0x0","gasUsed":"0x0","timestamp":"0x63f6ddb5","extraData":"0x","mixHash":"0x0000000000000000000000000000000000000000000000000000000000000000","nonce":"0x0000000000000000","baseFeePerGas":"0x3b9aca00","hash":"0x6efc61b53ed42c5c6fcc2e554ce00405fb241b48455db0ec614b7e67f9220e78"}}}
```
{% endcode %}
