# /getBlockTransactions

Get transactions of the given block.



**Parameters:**

**workchain - integer,** Workchain id to look up block in

**shard - integer,** Shard id to look up block in

**seqno - integer,** Masterchain seqno to fetch shards of.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getBlockTransactions?workchain=-1&shard=8000000000000000&seqno=39984096&count=40' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "blocks.transactions",
    "id": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984096,
      "root_hash": "b26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEM=",
      "file_hash": "lLylrj7eZn0TSNxpg4yovJJ4x/ILgeeJ3byS6MFVTJw="
    },
    "req_count": 40,
    "incomplete": false,
    "transactions": [
      {
        "@type": "blocks.shortTxId",
        "mode": 135,
        "account": "-1:3333333333333333333333333333333333333333333333333333333333333333",
        "lt": "48756940000001",
        "hash": "RzoRGcEyx5Ia5tEKUWlCpFbg8B0scpuXSyNXf9a4Nsk="
      },
      {
        "@type": "blocks.shortTxId",
        "mode": 135,
        "account": "-1:3333333333333333333333333333333333333333333333333333333333333333",
        "lt": "48756940000002",
        "hash": "0kwvliWmBxHEXXWVNhNfBZsQFGaWejcojKq79d3Im+A="
      },
      {
        "@type": "blocks.shortTxId",
        "mode": 135,
        "account": "-1:5555555555555555555555555555555555555555555555555555555555555555",
        "lt": "48756940000003",
        "hash": "AKRX7V8G5q2Jr9gxsZkkWu8xsnORTIB08SWuMt59Src="
      }
    ],
    "@extra": "1724745508.148041:2:0.6018950252728974"
  }
}
```
{% endcode %}
