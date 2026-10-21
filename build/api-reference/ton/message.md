# message

Send an external message to the TON network.

{% hint style="info" %}
The message must be a fully serialized, signed external message (boc, base64). On success the endpoint returns the message hash, which can be polled with `/transactionsByMessage` once the message is executed. An unparsable body returns `500 Failed to unpack Message`.
{% endhint %}

**Parameters**

Request body (`application/json`):

* **`boc`** — string. Base64 boc of a fully serialized and signed external message.

**Returns**

* `message_hash` — string
* `message_hash_norm` — string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/message' \
  -H 'Content-Type: application/json' \
  --data '{"boc": "<base64-encoded boc of the signed external message>"}'

// Result
{
  "message_hash": "<base64 hash of the accepted message>",
  "message_hash_norm": "<base64url hash of the accepted message>"
}
```
{% endcode %}
