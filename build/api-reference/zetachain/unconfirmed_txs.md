---
description: Get list of unconfirmed transactions
---

# /unconfirmed\_txs

#### **Parameters:**

**limit- int**, Maximum number of unconfirmed transactions to return (max 100, Default 30)

#### Example:

<pre class="language-json" data-overflow="wrap"><code class="lang-json">// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/&#x3C;your-api-key>/unconfirmed_txs

// Result
<strong>{
</strong>    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "n_txs": "2",
        "total": "2",
        "total_bytes": "1136",
        "txs": [
            "CrwBCrkBCjMvemV0YWNoYWluLnpldGFjb3JlLmNyb3NzY2hhaW4uTXNnQWRkVG9PdXRUeFRyYWNrZXISgQEKK3pldGExNXE1cnFwNDBxMmtmN25tZXZoc3R4Nmx1eDRlMjJudXpwdWxucjkSCkJTQ1RFU1RORVQY2KxQIkIweDkzMmM4ODRiMDM1NTA0ODZlODYwZTQ0MDVkMGY5YmZlOTBhYmRlYWJmNGRlZWI4YmI1ZmZlNDA0YzQ4NzJhOTgSawpTCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohA8lRScBvu/kbeTto6Lg8z8kqUka+56u/niaLTMP/0PqCEgQKAggBGNmm4QcSFAoOCgVhemV0YRIFNDAwMDAQwJoMGkA3xVPxQfUI5MQE1fuDrH/91Qv7TCflMTzyQgcnadLLOnWHOx8q9pJCWUvw5hVEFBfwMxVRTPC1iBGbCuYLuI8j",
            "Cs8ECswECjkvemV0YWNoYWluLnpldGFjb3JlLmNyb3NzY2hhaW4uTXNnVm90ZU9uT2JzZXJ2ZWRJbmJvdW5kVHgSjgQKK3pldGExdDR6a205OHdmNjI1azd5NW50djg1MHJxenkzcmQ0YTBzdjZ1ODQSKjB4ODM3ODBiRWM0Q2Y3NjM4NUZCMjhhZjk3NzdEMkYzYUUxODc3NzFmZBoKQlNDVEVTVE5FVCIqMHg4Mzc4MGJFYzRDZjc2Mzg1RkIyOGFmOTc3N0QyRjNhRTE4Nzc3MWZkKgRaRVRBMg8xODkwMDAwMDAwMDAwMDBC6AE3MWVjNWMwNWFhNjY5YzQ5MjI1NjljMWQzM2Y3YTgxYWFhMjE4MTM4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwZDk3YjFkZTM2MTllZDJjNmJlYjM4NjAxNDdlMzBjYThhN2RjOTg5MTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDgzNzgwYmVjNGNmNzYzODVmYjI4YWY5Nzc3ZDJmM2FlMTg3NzcxZmQwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwSkIweDk1MjFlYjQ5MzI4ZjE3NTBhZjFlZGVmOTZiYzE1MDM5MjgyNWI1ZmQwY2YxYjlkNmNiOTk5YmM4NGQxODQ0ZDBQ29XMDViQvwVgAWoqMHg4Mzc4MGJFYzRDZjc2Mzg1RkIyOGFmOTc3N0QyRjNhRTE4Nzc3MWZkEmwKUwpGCh8vY29zbW9zLmNyeXB0by5zZWNwMjU2azEuUHViS2V5EiMKIQISsYpS9GiPgwi4LzoKWeLqsiwDALtekZaSKJHR36ArMhIECgIIARjb7N0GEhUKDgoFYXpldGESBTQwMDAwEICt4gQaQCmTWhu/LaOcGNLxVfq/V0cA/5B28znE3p7B+ycnQpjmWvrjH6Bivuqkb8RaTNsGLg7mWkxoGciiSH6BgMHvArM="
        ]
    }
}   
</code></pre>
