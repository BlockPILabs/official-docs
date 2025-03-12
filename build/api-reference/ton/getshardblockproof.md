# /getShardBlockProof

Get merkle proof of shardchain block.



**Parameters:**

**workchain - integer**, Block workchain id

**shard - integer**, Block shard id

**seqno - integer**,  Block seqno

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getShardBlockProof?workchain=-1&shard=8000000000000000&seqno=39984096' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "blocks.shardBlockProof",
    "from": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984101,
      "root_hash": "eglRQPq+0HaEhQAkQdmnfeQrx2k1l1s1bs2Na6cEDUM=",
      "file_hash": "iRMUKPb/t/FreFjE/37ZTL6RAgTjLziZKuXrb4fBK3Y="
    },
    "mc_id": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984096,
      "root_hash": "b26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEM=",
      "file_hash": "lLylrj7eZn0TSNxpg4yovJJ4x/ILgeeJ3byS6MFVTJw="
    },
    "links": [],
    "mc_proof": [
      {
        "@type": "blocks.blockLinkBack",
        "to_key_block": false,
        "from": {
          "@type": "ton.blockIdExt",
          "workchain": -1,
          "shard": "-9223372036854775808",
          "seqno": 39984101,
          "root_hash": "eglRQPq+0HaEhQAkQdmnfeQrx2k1l1s1bs2Na6cEDUM=",
          "file_hash": "iRMUKPb/t/FreFjE/37ZTL6RAgTjLziZKuXrb4fBK3Y="
        },
        "to": {
          "@type": "ton.blockIdExt",
          "workchain": -1,
          "shard": "-9223372036854775808",
          "seqno": 39984096,
          "root_hash": "b26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEM=",
          "file_hash": "lLylrj7eZn0TSNxpg4yovJJ4x/ILgeeJ3byS6MFVTJw="
        },
        "dest_proof": "te6ccgECBwEAAUcACUYDb26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEMAFgEkEBHvVar///8RAgMEBQGgm8ephwAAAAAEAQJiG+AAAAABAP////8AAAAAAAAAAGbNgusAACxYHBbLAAAALFgcFssEhnXR4wAJKjkCYhvXAmIZsMQAAAAIAAAAAAAAAe4GKEgBAbV+dyl7df2U+EcX/zipKYXLUEeeyKfnfozOhJsehHJBAAMoSAEBcW0pMPKCca+0I1+J1mXLTnW7nifvLD65/7XnCu82Yn0AFShIAQHA/OZgJdXkF3mNttsTd/TtRP2k6LL+kSNhvV+z/+k5QwAIAJgAACxYG9nCBAJiG98l+EwUbKSNy6Cv08/5us6wn1gxWKk+o1T+WHe38+Zp2jhA1tf3EiPiLTk5OM3LRJAD8JsL4WUGRtrCpJIiS0xk",
        "proof": "te6ccgECCQEAAfoACUYDeglRQPq+0HaEhQAkQdmnfeQrx2k1l1s1bs2Na6cEDUMAFgEkEBHvVar///8RAgMEBQGgm8ephwAAAAAEAQJiG+UAAAABAP////8AAAAAAAAAAGbNg3QAACxYHOxqgAAALFgc7GqEAqbePwAJKjoCYhvhAmIZsMQAAAAIAAAAAAAAAe4GKEgBAXDZdO9ozkURTK/BGsTdwN7VODWDJtaWsJ/Vm3SvXS/OAAMqigQzi/ffFANoQrv5Y2nsXCSV8FdwC5+1iHheoZz+2QgN9YvjXiu1KiiMe1n5pZxToHH0UHhih4BuNTMqKf73l5YFAW8BbwcIKEgBATLhLhy1Bg3mEToZmVw+noVrrxgex0rZ5uKceOCFdJrBAAgAmAAALFgczeYEAmIb5LX52+8Oq4CsnVF2yH/8qqpJ+o/84L40Lyead2OY2SHduwIkYtAxpU+IzuHOEcXitGCQsevdWzHPFnmQ5Oc0vVZojAEDM4v33xQDaEK7+WNp7FwklfBXcAuftYh4XqGc/tkIDfWkww/Ynm5n4bJfw9qSFu83rshjaK2Tu4qLyV3DQxJuxAFvABRojAEDi+NeK7UqKIx7WfmlnFOgcfRQeGKHgG41Myop/veXlgXPBxUY3wQ+MrbfJihAeWlCPZpXmbTkka+A/37E7EJ/vwFvABQ=",
        "state_proof": "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"
      }
    ],
    "@extra": "1724744622.3789763:6:0.1414000696427048"
  }
}
```
{% endcode %}
