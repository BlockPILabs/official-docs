# topaccountsbybalance

Return accounts sorted by balance in descending order.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* \`\` — array of objects with fields `account`, `balance`

#### Example:

\{% code overflow="wrap" %\}

```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/topAccountsByBalance?limit=2'

// Result
[
  {
    "account": "-1:3333333333333333333333333333333333333333333333333333333333333333",
    "balance": "1376062616412892124"
  }
]
```
