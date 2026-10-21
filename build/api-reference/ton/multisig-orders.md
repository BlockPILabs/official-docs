# multisig orders

Query multisig orders that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`address`** — array of strings, optional. Order address in any form. Maximum: 1024 addresses.
* **`multisig_address`** — array of strings, optional. Address of the corresponding multisig wallet in any form. Maximum: 1024 addresses.
* **`parse_actions`** — boolean, optional, default `False`. Parse order actions.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort orders by `last_transaction_lt`.

**Returns**

* `address_book` — object
* `orders` — array of objects with fields `actions`, `address`, `approvals_mask`, `approvals_num`, `code_hash`, `data_hash`, `expiration_date`, `last_transaction_lt`, `multisig_address`, `order_boc`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/multisig/orders?address=0%3AED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7'

// Result
{
  "orders": [],
  "address_book": {}
}
```
{% endcode %}
