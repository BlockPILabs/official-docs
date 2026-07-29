---
description: >-
  Creates new message call transaction or a contract creation for signed
  transactions.
---

# eth\_sendRawTransaction

#### **Parameters:**

**DATA** - The signed transaction data.

#### **Returns:**

**DATA, 32 Bytes** - the transaction hash, or the zero hash if the transaction is not yet available.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params":["0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"],"id":1}'

// Result

```
{% endcode %}

{% hint style="info" %}
Polygon network now supports MEV protection. This feature affects the eth\_sendRawTransaction method. Once enabled, each transaction submitted via sendRawTransaction will be charged at 25,000 RU per request.

The fee exists because MEV protection in the Polygon ecosystem is exclusively provided by the Polygon official as a paid service — there is no alternative third-party option available. Although this comes with an additional cost, the feature provides 100% protection against MEV attacks, safeguarding traders from sandwich attacks, front-running, and other malicious activities. It is also backed by Polygon's official endorsement, ensuring reliability and security.
{% endhint %}
