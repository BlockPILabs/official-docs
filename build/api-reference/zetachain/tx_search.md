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
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/&#x3C;your-api-key>/tx_search?query=%22tx.height%3D2115661%22

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "txs": [
            {
                "hash": "46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891",
                "height": "2115661",
                "index": 0,
                "tx_result": {
                    "code": 0,
                    "data": "CjsKOS96ZXRhY2hhaW4uemV0YWNvcmUuY3Jvc3NjaGFpbi5Nc2dWb3RlT25PYnNlcnZlZEluYm91bmRUeA==",
                    "log": "[
                        ......
<strong>                    ],
</strong><strong>                    "info": "",
</strong>                    "gas_wanted": "10000000",
                    "gas_used": "8837225",
                    "events": [
                        {
                            "type": "coin_spent",
                            "attributes": [
                                {
                                    "key": "c3BlbmRlcg==",
                                    "value": "emV0YTFrazlqcXd1ZmhjZXZlYWtjYWp2MzB3aGo2OGcyMjhkY2NzMnhlNQ==",
                                    "index": true
                                },
                                {
                                    "key": "YW1vdW50",
                                    "value": "NDAwMDBhemV0YQ==",
                                    "index": true
                                }
                            ]
                        },
                        {
                            "type": "coin_received",
                            "attributes": [
                                {
                                    "key": "cmVjZWl2ZXI=",
                                    "value": "emV0YTE3eHBmdmFrbTJhbWc5NjJ5bHM2Zjg0ejNrZWxsOGM1bHhhZDQzZA==",
                                    "index": true
                                },
                                {
                                    "key": "YW1vdW50",
                                    "value": "NDAwMDBhemV0YQ==",
                                    "index": true
                                }
                            ]
                        },
                        ......
                     ],
                    "codespace": "observer"
                },
                "tx": "Cp0CCpoCCjovemV0YWNoYWluLnpldGFjb3JlLmNyb3NzY2hhaW4uTXNnVm90ZU9uT2JzZXJ2ZWRPdXRib3VuZFR4EtsBCit6ZXRhMXQ0emttOTh3ZjYyNWs3eTVudHY4NTBycXp5M3JkNGEwc3Y2dTg0EkIweDhiZDI5ZWU2OWIyMjYyZGM5ZjEyYzhlNWQxMGIyOWZlNGI2MzVjMWZjMTgxMGJiMjM1NmEyODBjM2I3NDRlNDYaQjB4NTBmMzI4ODJhYjQ0YjQ4ZTFmMWRmNjdlMmM1OWU3YTQ1MmNjODI0ZTM0MmY0ODAyZTI4ZWZhNTJjMzgwNmI3MyCO+ZUEKg84NTUyNDE4MzQ2MjY4MjQwAToGR09FUkxJQLy/OkgBEmsKUwpGCh8vY29zbW9zLmNyeXB0by5zZWNwMjU2azEuUHViS2V5EiMKIQISsYpS9GiPgwi4LzoKWeLqsiwDALtekZaSKJHR36ArMhIECgIIARjGj90GEhQKDgoFYXpldGESBTQwMDAwEMCaDBpAvkn7x4DzQ30oeiEAkF2yJiO7dJdHpubXboIV7D1+SRZU/hbjGresUH3cI2xhrpaWPAaHM2m/3+gWVFBWNrmxxA=="
            }
        ],
        "total_count": "73"
    }
}          
</code></pre>
