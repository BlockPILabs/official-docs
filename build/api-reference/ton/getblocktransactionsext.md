# /getBlockTransactionsExt

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
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getBlockTransactionsExt?workchain=-1&shard=8000000000000000&seqno=39984096&count=40' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "blocks.transactionsExt",
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
        "@type": "raw.transaction",
        "address": {
          "@type": "accountAddress",
          "account_address": "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF"
        },
        "utime": 1724744427,
        "data": "te6cckECBgEAASwAA69zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzAAAsWBwWywFasDdwrFP+Ct1DUZ8E6dkyE1E0qNEMcw3U5Z/AIV+fAwAALFgb2cICZs2C6wABQIAQIDAAEgAIJyeCnCsfoPoq6guy3J9EugcHoRfAQNxvzoihR4pR+6k/zEOJtbaWuxu8c0lOpEaUNnbnx9GRcx45lUpmHyBGs+5AIFIDAkBAUAoERmcBCwdgAAAAAAAAAAALUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvAAAAAAAAAAAAAAAABLUUtpEnlC4z33SeGHxRhIq/htUa7i3D8ghbwxhQTn44E3yoKBA==",
        "transaction_id": {
          "@type": "internal.transactionId",
          "lt": "48756940000001",
          "hash": "RzoRGcEyx5Ia5tEKUWlCpFbg8B0scpuXSyNXf9a4Nsk="
        },
        "fee": "0",
        "storage_fee": "0",
        "other_fee": "0",
        "out_msgs": [],
        "account": "-1:3333333333333333333333333333333333333333333333333333333333333333"
      },
      {
        "@type": "raw.transaction",
        "address": {
          "@type": "accountAddress",
          "account_address": "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF"
        },
        "utime": 1724744427,
        "data": "te6cckECBwEAAYwAA69zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzAAAsWBwWywJHOhEZwTLHkhrm0QpRaUKkVuDwHSxym5dLI1d/1rg2yQAALFgcFssBZs2C6wABQIAQIDAQGgBACCcsQ4m1tpa7G7xzSU6kRpQ2dufH0ZFzHjmVSmYfIEaz7kSbFGUIW/3qMAAATl2NUQQOED3ryvNPIrua46UDXQgAYCEQQJQbKYXIUYEQUGAK1p/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABP8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM1BsphchQAAAAWLA4LZYAzZsF1kAAoEKvcBCwdgAAAAAAAAAAAGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvAAAAAAAAAAAAAAAABLUUtpEnlC4z33SeGHxRhIq/htUa7i3D8ghbwxhQTn44Ef1g1rg==",
        "transaction_id": {
          "@type": "internal.transactionId",
          "lt": "48756940000002",
          "hash": "0kwvliWmBxHEXXWVNhNfBZsQFGaWejcojKq79d3Im+A="
        },
        "fee": "0",
        "storage_fee": "0",
        "other_fee": "0",
        "in_msg": {
          "@type": "raw.message",
          "source": {
            "@type": "accountAddress",
            "account_address": "Ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAU"
          },
          "destination": {
            "@type": "accountAddress",
            "account_address": "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF"
          },
          "value": "29165187604",
          "fwd_fee": "0",
          "ihr_fee": "0",
          "created_lt": "48756940000000",
          "body_hash": "lqKW0iTyhcZ77pPDD4owkVfw2qNdxbh+QQt4YwoJz8c=",
          "msg_data": {
            "@type": "msg.dataRaw",
            "body": "te6cckEBAQEAAgAAAEysuc0=",
            "init_state": ""
          }
        },
        "out_msgs": [],
        "account": "-1:3333333333333333333333333333333333333333333333333333333333333333"
      },
      {
        "@type": "raw.transaction",
        "address": {
          "@type": "accountAddress",
          "account_address": "Ef9VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVbxn"
        },
        "utime": 1724744427,
        "data": "te6cckECBgEAASwAA691VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVAAAsWBwWywOUHUXFV0BZwC1S62klX+y1XLNEHB9qOLaaOBqK9OgaJAAALFgb2cIDZs2C6wABQIAQIDAAEgAIJyD/qWUlHdP4D4qUlxuiBg/9DllUSMYlvd7a7edNStIzckB3DHOBQ2ASMDVM43C7HIhkbn7Dx0GfE2i/2WgREVPgIFMDAkBAUAoEE20BCwdgAAAAAAAAAAAC4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvAAAAAAAAAAAAAAAABLUUtpEnlC4z33SeGHxRhIq/htUa7i3D8ghbwxhQTn44End+r9A==",
        "transaction_id": {
          "@type": "internal.transactionId",
          "lt": "48756940000003",
          "hash": "AKRX7V8G5q2Jr9gxsZkkWu8xsnORTIB08SWuMt59Src="
        },
        "fee": "0",
        "storage_fee": "0",
        "other_fee": "0",
        "out_msgs": [],
        "account": "-1:5555555555555555555555555555555555555555555555555555555555555555"
      }
    ],
    "@extra": "1724745572.6994271:5:0.5335802192168009"
  }
}
```
{% endcode %}
