# /getAddressBalance

Get transaction history of a given address.



**Parameters:**

**address - string,** Identifier of target TON account in any form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getAddressBalance?address=UQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVxtU' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": "14020735"
}
```
{% endcode %}
