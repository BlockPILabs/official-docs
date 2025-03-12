---
description: GetTxsEvent fetches txs by event.
---

# /cosmos/tx/v1beta1/txs?event={event}

#### **Parameters:**

**event - array\[string]**, events is the list of transaction event type.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/tx/v1beta1/txs?events={events}

// Result
{
  "txs": [
    {
      "body": {
        "messages": [
          {
            "@type": "string"
          }
        ],
        "memo": "string",
        "timeout_height": "string",
        "extension_options": [
          {
            "@type": "string"
          }
        ],
        "non_critical_extension_options": [
          {
            "@type": "string"
          }
        ]
      },
      "auth_info": {
        "signer_infos": [
          {
            "public_key": {
              "@type": "string"
            },
            "mode_info": {
              "single": {
                "mode": "SIGN_MODE_UNSPECIFIED"
              },
              "multi": {
                "bitarray": {
                  "extra_bits_stored": 0,
                  "elems": "string"
                },
                "mode_infos": [
                  null
                ]
              }
            },
            "sequence": "string"
          }
        ],
        "fee": {
          "amount": [
            {
              "denom": "string",
              "amount": "string"
            }
          ],
          "gas_limit": "string",
          "payer": "string",
          "granter": "string"
        }
      },
      "signatures": [
        "string"
      ]
    }
  ],
  "tx_responses": [
    {
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
  ],
  "pagination": {
    "next_key": "string",
    "total": "string"
  }
}
```
{% endcode %}
