# multisig wallets

Query multisig contracts that match the specified filters, optionally including their orders.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`address`** — array of strings, optional. Multisig contract address in any form. Maximum: 1024 addresses.
* **`wallet_address`** — array of strings, optional. Address of a signer or proposer wallet in any form. Maximum: 1024 addresses.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort multisigs by `last_transaction_lt`.
* **`include_orders`** — boolean, optional, default `True`. Include multisig orders.

**Returns**

* `address_book` — object
* `multisigs` — array of objects with fields `address`, `code_hash`, `data_hash`, `last_transaction_lt`, `next_order_seqno`, `orders`, `proposers`, `signers`, `threshold`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/multisig/wallets?address=0%3AED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7'

// Result
{
  "multisigs": [],
  "address_book": {}
}
```
{% endcode %}
