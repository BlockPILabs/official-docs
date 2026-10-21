# walletstates

Query wallet information for the specified addresses.

**Parameters**

* **`address`** — array of strings, required. List of addresses in any form. Maximum: 1000 addresses.

**Returns**

* `address_book` — object
* `metadata` — object
* `wallets` — array of objects with fields `address`, `balance`, `code_hash`, `extra_currencies`, `is_signature_allowed`, `is_wallet`, `last_transaction_hash`, `last_transaction_lt`, `seqno`, `status`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/walletStates?address=0%3AF785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78'

// Result
{
  "wallets": [
    {
      "address": "0:ED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7",
      "is_wallet": false,
      "balance": "1246187124150386674",
      "status": "active",
      "code_hash": "gwyZpEfQl0222G7X2J/k8tLsIjWMtkKH4tMeVj695Uc=",
      "last_transaction_hash": "2On+zSO62+DjyNBNGJOkCYgtCs84pVcTpbNmCZGsFKA=",
      "last_transaction_lt": "111285831000019"
    }
  ],
  "address_book": {
    "0:ED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7": {
      "user_friendly": "EQDtFpEwcFAEcRe5mLVh2N6C0x-_hJEM7W61_JLnSF74p4q2",
      "domain": null,
      "interfaces": [
        "locker"
      ]
    }
  },
  "metadata": {}
}
```
{% endcode %}
