# /getConfigParam

Get config by id.



**Parameters:**

**config\_id - integer,** Config id

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getConfigParam?config_id=1' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "configInfo",
    "config": {
      "@type": "tvm.cell",
      "bytes": "te6cckEBAQEAIgAAQDMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzwqnziA=="
    },
    "@extra": "1724745975.322405:9:0.07466730062972271"
  }
}
```
{% endcode %}
