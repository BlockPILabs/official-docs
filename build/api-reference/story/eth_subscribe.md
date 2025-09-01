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
wscat -c wss://0g-galileo.blockpi.network/v1/ws/<your-api-key>

//create an event
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["newHeads"]}

// Result
{...}
```
{% endcode %}
