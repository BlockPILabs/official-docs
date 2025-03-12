# /runGetMethod

Run get method on smart contract.



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'POST' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getConfigAll' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "address": "string",
  "method": "string",
  "stack": [
    [
      "string"
    ]
  ],
  "seqno": 0
}'

// Result

```
{% endcode %}
