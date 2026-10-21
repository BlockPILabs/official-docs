# messages

Query messages that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`msg_hash`** — array of strings, optional. Message hash in hex, base64, or base64url form.
* **`body_hash`** — string, optional. Hash of message body.
* **`source`** — string, optional. Source account address in hex, base64, or base64url form. Set this parameter to `null` to return external messages.
* **`destination`** — string, optional. Destination account address in hex, base64, or base64url form. Set this parameter to `null` to return log messages.
* **`opcode`** — string, optional. Opcode of message in hex or signed 32-bit decimal form.
* **`start_utime`** — integer, optional. Query messages where `created_at` is at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query messages where `created_at` is at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query messages where `created_lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query messages where `created_lt` is at or below the specified value.
* **`direction`** — string, optional. Direction of the message.
* **`exclude_externals`** — boolean, optional. Exclude external messages.
* **`only_externals`** — boolean, optional. Return only external messages.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort messages by `lt`. To return the latest messages with `sort=desc`, set `start_lt` to `1`.

**Returns**

* `address_book` — object
* `messages` — array of objects with fields `bounce`, `bounced`, `created_at`, `created_lt`, `decoded_opcode`, `destination`, `extra_flags`, `fwd_fee`, `hash`, `hash_norm`
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/messages?limit=2'

// Result
{
  "messages": [
    {
      "hash": "l3HF8K8LzkMd7nus3J6NaYvLXzSi87NlDuE4+C7dKl0=",
      "source": "-1:0000000000000000000000000000000000000000000000000000000000000000",
      "destination": "-1:3333333333333333333333333333333333333333333333333333333333333333",
      "value": "2701168584",
      "value_extra_currencies": {},
      "fwd_fee": "0",
      "ihr_fee": "0",
      "extra_flags": "0",
      "created_lt": "111332906000000",
      "created_at": "1792550072",
      "opcode": null,
      "decoded_opcode": null,
      "ihr_disabled": true,
      "bounce": true,
      "bounced": false,
      "import_fee": null,
      "in_msg_tx_hash": "QHGtdR0kHafjaG7foq2IXoiSGr69dz8Ul3TpQKebO/k=",
      "message_content": {
        "hash": "lqKW0iTyhcZ77pPDD4owkVfw2qNdxbh+QQt4YwoJz8c=",
        "body": "te6cckEBAQEAAgAAAEysuc0=",
        "decoded": {
          "@type": "empty_cell"
        }
      },
      "init_state": null
    }
  ],
  "address_book": {
    "-1:0000000000000000000000000000000000000000000000000000000000000000": {
      "user_friendly": "Ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAU",
      "domain": null,
      "interfaces": []
    },
    "-1:3333333333333333333333333333333333333333333333333333333333333333": {
      "user_friendly": "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF",
      "domain": null,
      "interfaces": null
    },
    "0:7914AC998024F7C5E5BC6C332EFCC15DD823D88E564FF616233FC947E52E5E0C": {
      "user_friendly": "UQB5FKyZgCT3xeW8bDMu_MFd2CPYjlZP9hYjP8lH5S5eDFlB",
      "domain": null,
      "interfaces": []
    },
    "0:7CEB78526D2E6D5F9CADC4F0C823EA59EAEF72054916CE0C5A715C74F82F2534": {
      "user_friendly": "EQB863hSbS5tX5ytxPDII-pZ6u9yBUkWzgxacVx0-C8lNNrq",
      "domain": null,
      "interfaces": [
        "jetton_wallet_governed"
      ]
    }
  }
}
```
{% endcode %}
