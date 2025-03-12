# /getMasterchainBlockSignatures

Get up-to-date masterchain state.



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getMasterchainBlockSignatures?seqno=39984096' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "blocks.blockSignatures",
    "id": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984096,
      "root_hash": "b26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEM=",
      "file_hash": "lLylrj7eZn0TSNxpg4yovJJ4x/ILgeeJ3byS6MFVTJw="
    },
    "signatures": [
      {
        "@type": "blocks.signature",
        "node_id_short": "mBiFBlrq63KkEeQT/8rfkH36W5P3+j/+zx292zpTzZQ=",
        "signature": "+f+5nzW4tfZeVzWaVEbBmndpCWGHnoRQYFG3KjlcbP23sNSRTIf6SPgUaNfQ8W9gpvUROAeRckI79xCumspDAQ=="
      },
      ......
      
```
{% endcode %}
