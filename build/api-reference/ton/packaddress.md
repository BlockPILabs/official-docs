# /packAddress

Convert an address from raw to human-readable format.



**Parameters:**

**address - string,** Identifier of target TON account in raw form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/packAddress?address=0%3A83DFD552E63729B472FCBCC8C45EBCC6691702558B68EC7527E1BA403A0F31A8' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"
}
```
{% endcode %}
