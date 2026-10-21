# rungetmethod

Run a get method for a smart contract. The stack supports only `num`, `cell`, and `slice` types:

```
[
{
"type": "num",
"value": "0x12a"
},
{
"type": "cell",
"value": "te6..." // base64-encoded BoC with cell
},
{
"type": "slice",
"value": "te6..." // base64-encoded BoC with slice
}
]
```

**Parameters**

Request body (`application/json`):

* **`address`** — string. Contract address in any form.
* **`method`** — string. Get-method name, e.g. `get_wallet_data`.
* **`stack`** — array of objects. Arguments as an array of `{"type":"num|cell|slice","value":...}` objects.

**Returns**

* `address` — string
* `method` — string
* `stack` — array of objects with fields `type`, `value`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/runGetMethod' \
  -H 'Content-Type: application/json' \
  --data '{"address": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs", "method": "get_wallet_data", "stack": []}'

// Result
{
  "gas_used": 470,
  "exit_code": 11,
  "stack": [
    {
      "type": "num",
      "value": "0x17b02"
    }
  ]
}
```
{% endcode %}
