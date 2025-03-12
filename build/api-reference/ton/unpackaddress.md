# /unpackAddress

Convert an address from human-readable to raw format.



**Parameters:**

**address - string,** Identifier of target TON account in user-friendly form

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/unpackAddress?address=EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": "0:83dfd552e63729b472fcbcc8c45ebcc6691702558b68ec7527e1ba403a0f31a8"
}
```
{% endcode %}
