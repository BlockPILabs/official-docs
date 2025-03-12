---
description: Get list of unconfirmed transactions
---

# /unconfirmed\_txs

#### **Parameters:**

**limit- int**, Maximum number of unconfirmed transactions to return (max 100, Default 30)

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/unconfirmed_txs

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "n_txs": "7",
        "total": "7",
        "total_bytes": "37950",
        "txs": [
            "ClQKUgobL2Nvc21vcy5nb3YudjFiZXRhMS5Nc2dWb3RlEjMIZxItY29zbW9zMXNuZms3NnlxZWc5Z2Nzam5rNmd4cXpoZjI5eHo3cHpxZXZjczg3GAESZwpRCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohAtnfUncaFoD9LSd3+fiIq2uM4kx+eH7zf27k7FENLbUYEgQKAggBGK0CEhIKDAoFdWF0b20SAzIwNBC2+wQaQCmmYn5fl7AoDioDAtN6H34ueBX+7vbwRyCg53cj6WrtNzmitcmRxJVb8nI+lW/yEjCGBnI4lYYFnyk0SzIBe9A=",
            ......
        ]
    }
}       
```
{% endcode %}
