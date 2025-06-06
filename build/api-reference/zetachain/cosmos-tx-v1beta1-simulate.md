---
description: Simulate simulates executing a transaction for estimating gas usage.
---

# /cosmos/tx/v1beta1/simulate

#### **Parameters:**

**body - object**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/tx/v1beta1/simulate
--data
{
  "tx": {
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
  },
  "tx_bytes": "string"
}

// Result
{
  "gas_info": {
    "gas_wanted": "string",
    "gas_used": "string"
  },
  "result": {
    "data": "string",
    "log": "string",
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
