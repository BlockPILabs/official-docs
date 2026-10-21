# pendingtraces

Query pending traces that match the specified filters.

**Parameters**

* **`account`** — string, optional. List of account addresses to query. Provide addresses in hex, base64, or base64url form.
* **`ext_msg_hash`** — array of strings, optional. Find traces by external hash.

**Returns**

* `address_book` — object
* `metadata` — object
* `traces` — array of objects with fields `actions`, `end_lt`, `end_utime`, `external_hash`, `is_incomplete`, `mc_seqno_end`, `mc_seqno_start`, `start_lt`, `start_utime`, `trace`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/pendingTraces?account=0%3AF785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78'

// Result
{
  "traces": [],
  "address_book": {},
  "metadata": {}
}
```
{% endcode %}
