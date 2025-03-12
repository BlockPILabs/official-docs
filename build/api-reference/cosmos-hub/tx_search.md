---
description: >-
  Search for transactions w/ their results.  See /subscribe for the query
  syntax.
---

# /tx\_search

#### **Parameters:**

**query - string**, Query

#### Example:

<pre class="language-json" data-overflow="wrap"><code class="lang-json">// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/&#x3C;your-api-key>/tx_search?query=%22tx.height%3D14183822%22

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "txs": [
            {
                "hash": "547DC59DD6EE54082183A5F75F1D350BE4D271825BB75C6A626F74DAE2FA2489",
                "height": "14183822",
                "index": 0,
                "tx_result": {
                    "code": 0,
                    "data": "Ch4KHC9jb3Ntb3MuYmFuay52MWJldGExLk1zZ1NlbmQ=",
                    "log": "[{\"events\":[{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"cosmos1f0d77kqccjcz95r4py478zppgwl3pl8w4x9s0p\"},{\"key\":\"amount\",\"value\":\"1719939uatom\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"cosmos1s5z672rlcfy596xvm3q2c4phfhg9pk704654af\"},{\"key\":\"amount\",\"value\":\"1719939uatom\"}]},{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"/cosmos.bank.v1beta1.MsgSend\"},{\"key\":\"sender\",\"value\":\"cosmos1s5z672rlcfy596xvm3q2c4phfhg9pk704654af\"},{\"key\":\"module\",\"value\":\"bank\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"cosmos1f0d77kqccjcz95r4py478zppgwl3pl8w4x9s0p\"},{\"key\":\"sender\",\"value\":\"cosmos1s5z672rlcfy596xvm3q2c4phfhg9pk704654af\"},{\"key\":\"amount\",\"value\":\"1719939uatom\"}]}]}]",
                    "info": "",
                    "gas_wanted": "91770",
                    "gas_used": "69111",
                    "events": [
                        {
                            "type": "coin_spent",
                            "attributes": [
                                {
                                    "key": "c3BlbmRlcg==",
                                    "value": "Y29zbW9zMXM1ejY3MnJsY2Z5NTk2eHZtM3EyYzRwaGZoZzlwazcwNDY1NGFm",
                                    "index": true
                                },
                                {
                                    "key": "YW1vdW50",
                                    "value": "MjI5NXVhdG9t",
                                    "index": true
                                }
                            ]
                        },
                        ......
<strong>                    ],
</strong>                    "codespace": ""
                },
                "tx": "CqQBCqEBCiUvY29zbW9zLnN0YWtpbmcudjFiZXRhMS5Nc2dVbmRlbGVnYXRlEngKLWNvc21vczFkanpjN2w1c3YyYXpqcDgzbGc1dGF1czJuY3BoeWwzdW44eGNheBI0Y29zbW9zdmFsb3BlcjFsemhsbnBhaHZ6bndmdjRqbWF5MnRnYWhhNWttejVxeGVyYXJybBoRCgV1YXRvbRIIMTI0MDAwMDASZwpQCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohApSU8Gi2Qq3NuB1E8PxYnEEZQBTojTxS9eF8wzN9VZobEgQKAgh/GAwSEwoNCgV1YXRvbRIENjcxNhC9shAaQLW+MkV6xq5e6BrNA04oqWwl3H/AtZSNwfjdapeVqwyIBIl5x3twXBJRYgL+iLKHOFJXxEQj5Uv6aM0UHq6lY1Y="
            }
        ],
        "total_count": "5"
    }
}                        
</code></pre>
