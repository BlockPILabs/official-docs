# decode post

Decode opcodes and message bodies. Opcodes can be in hexadecimal (with or without the `0x` prefix) or decimal format. Bodies can be in base64 or hexadecimal format. Use POST for long parameters that may be truncated in GET requests.

**Parameters**

Request body (`application/json`):

* **`bodies`** — array of strings. Message bodies to decode, base64 or hex.
* **`opcodes`** — array of strings. Opcodes to decode, hex (with or without `0x`) or decimal.

**Returns**

* `bodies` — array of objects with fields
* `opcodes` — array of string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/decode' \
  -H 'Content-Type: application/json' \
  --data '{"opcodes": ["0x7362d09c"], "bodies": ["te6ccgEBAQEAAgAAAA=="]}'

// Result
{
  "opcodes": [
    "jetton_notify"
  ],
  "bodies": [
    {
      "@type": "empty_cell"
    }
  ]
}
```
{% endcode %}
