# /jsonRPC

All methods in the API are available through JSON-RPC protocol ([spec](https://www.jsonrpc.org/specification)).



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'POST' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/jsonRPC' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "string",
  "params": {},
  "id": "string",
  "jsonrpc": "string"
}'

// Result

```
{% endcode %}
