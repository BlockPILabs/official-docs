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
curl https://artela-testnet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params":["0xF549af21578Cfe2385FFD3488B3039fd9e52f006"],"id":1}'

// Result

```
{% endcode %}
