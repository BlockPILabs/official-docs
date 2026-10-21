# pendingtransactions

Query pending transactions that match the specified filters.

{% hint style="info" %}
Requirements: `/pendingTransactions` answers `404` with `{"error":"emulated traces not found"}` when the account has no in-flight transactions. A successful response has the same shape as `/transactions`.
{% endhint %}

**Parameters**

* **`account`** — array of strings, optional. List of account addresses to query. Provide addresses in hex, base64, or base64url form.
* **`trace_id`** — array of strings, optional. Find transactions by trace ID.

**Returns**

* `address_book` — object
* `transactions` — array of objects with fields `account`, `account_state_after`, `account_state_before`, `block_ref`, `description`, `emulated`, `end_status`, `finality`, `hash`, `in_msg`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/pendingTransactions?account=0%3AF785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78'

// Result
{
  "error": "emulated traces not found"
}
```
{% endcode %}
