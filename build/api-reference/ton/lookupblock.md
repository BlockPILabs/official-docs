# /lookupBlock

Look up block by either _seqno_, _lt_ or _unixtime_.



**Parameters:**

**workchain - integer,** Workchain id to look up block in

**shard - integer,** Shard id to look up block in

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/lookupBlock?workchain=-1&shard=8000000000000000&seqno=39984096' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "ton.blockIdExt",
    "workchain": -1,
    "shard": "-9223372036854775808",
    "seqno": 39984096,
    "root_hash": "b26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEM=",
    "file_hash": "lLylrj7eZn0TSNxpg4yovJJ4x/ILgeeJ3byS6MFVTJw=",
    "@extra": "1724745031.0833297:9:0.509065061818153"
  }
}
```
{% endcode %}
