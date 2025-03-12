# /estimateFee

Estimate fees required for query processing. _body_, _init-code_ and _init-data_ accepted in serialized format (b64-encoded).



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'POST' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/estimateFee' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "address": "string",
  "body": "string",
  "init_code": "",
  "init_data": "",
  "ignore_chksig": true
}'

// Result

```
{% endcode %}
