---
description: BroadcastTx broadcast transaction.
---

# /cosmos/tx/v1beta1/txs

#### **Parameters:**

**Body - object**, BroadcastTxRequest is the request type for the Service.BroadcastTxRequest RPC method.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/tx/v1beta1/txs
--data
{
  "tx_bytes": "string",
  "mode": "BROADCAST_MODE_UNSPECIFIED"
}

// Result
{
  "tx_response": {
    "height": "string",
    "txhash": "string",
    "codespace": "string",
    "code": 0,
    "data": "string",
    "raw_log": "string",
    "logs": [
      {
        "msg_index": 0,
        "log": "string",
        "events": [
          {
            "type": "string",
            "attributes": [
              {
                "key": "string",
                "value": "string"
              }
            ]
          }
        ]
      }
    ],
    "info": "string",
    "gas_wanted": "string",
    "gas_used": "string",
    "tx": {
      "@type": "string"
    },
    "timestamp": "string",
    "events": [
      {
        "type": "string",
        "attributes": [
          {
            "key": "string",
            "value": "string",
            "index": true
          }
        ]
      }
    ]
  }
}
```
{% endcode %}
