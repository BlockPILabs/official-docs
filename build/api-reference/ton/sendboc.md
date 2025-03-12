# /sendBoc

Send serialized boc file: fully packed and serialized external message to blockchain.



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'POST' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/sendBoc' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "boc": "string"
}'

// Result

```
{% endcode %}
