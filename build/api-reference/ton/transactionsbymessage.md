# transactionsbymessage

Get transactions whose inbound or outbound message has the specified hash.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`msg_hash`** — string, optional. Message hash in hex, base64, or base64url form.
* **`body_hash`** — string, optional. Hash of message body.
* **`opcode`** — string, optional. Opcode of message in hex or signed 32-bit decimal form.
* **`direction`** — string, optional. Direction of the message.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `transactions` — array of objects with fields `account`, `account_state_after`, `account_state_before`, `block_ref`, `description`, `emulated`, `end_status`, `finality`, `hash`, `in_msg`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/transactionsByMessage?msg_hash=l3HF8K8LzkMd7nus3J6NaYvLXzSi87NlDuE4%2BC7dKl0%3D'

// Result
{
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
    }
  }
}
```
{% endcode %}
