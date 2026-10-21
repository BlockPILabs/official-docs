# pendingactions

Query pending actions that match the specified filters.

**Parameters**

* **`account`** — string, optional. List of account addresses to query. Provide addresses in hex, base64, or base64url form.
* **`ext_msg_hash`** — array of strings, optional. Find actions by the external trace hash.
* **`supported_action_types`** — array of strings, optional. List supported action types.
* **`include_transactions`** — boolean, optional, default `False`. Include the `transactions_full` array with detailed transaction data for each action in the response.

**Returns**

* `actions` — array of objects with fields `accounts`, `action_id`, `details`, `end_lt`, `end_utime`, `finality`, `start_lt`, `start_utime`, `success`, `trace_end_lt`
* `address_book` — object
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/pendingActions?account=0%3AF785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78'

// Result
{
  "actions": [],
  "address_book": {},
  "metadata": {}
}
```
{% endcode %}
