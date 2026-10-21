# decode get

Decode opcodes and message bodies. Opcodes can be in hexadecimal (with or without the `0x` prefix) or decimal format. Bodies can be in base64 or hexadecimal format.

{% hint style="info" %}
Use the `POST` variant when the parameter list is long — GET query strings can be truncated by intermediaries.
{% endhint %}

**Parameters**

* **`opcodes`** — array of strings, optional. List of opcodes to decode in hexadecimal or decimal format.
* **`bodies`** — array of strings, optional. List of message bodies to decode in base64 or hexadecimal format.

**Returns**

* `bodies` — array of objects with fields
* `opcodes` — array of string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/decode?opcodes=0x7362d09c'

// Result
{
  "opcodes": [
    "jetton_notify"
  ],
  "bodies": []
}
```
{% endcode %}
