# /sendQuery

Send query - unpacked external message. This method takes address, body and init-params (if any), packs it to external message and sends to network. All params should be boc-serialized.



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'POST' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/sendQuery' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "address": "string",
  "body": "string",
  "init_code": "",
  "init_data": ""
}'

// Result

```
{% endcode %}
