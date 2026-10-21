# jetton wallets

Query jetton wallets that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`address`** — array of strings, optional. Jetton wallet address in any form. Maximum: 1000 addresses.
* **`owner_address`** — array of strings, optional. Address of the jetton wallet owner in any form. Maximum: 1000 addresses.
* **`jetton_address`** — array of strings, optional. Jetton master address in any form.
* **`exclude_zero_balance`** — boolean, optional. Exclude jetton wallets with a zero balance.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional. Sort jetton wallets by balance. Results may be inconsistent while paginating with `limit` and `offset`.

**Returns**

* `address_book` — object
* `jetton_wallets` — array of objects with fields `address`, `balance`, `code_hash`, `data_hash`, `jetton`, `last_transaction_lt`, `mintless_info`, `owner`
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/jetton/wallets?jetton_address=EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs&limit=2'

// Result
{
  "jetton_wallets": [
    {
      "address": "0:0000005CECBDC23E9FE415D530ADEE667EF35B4D3DB4CC49088B4F319179A86F",
      "balance": "0",
      "owner": "0:5E851231E85CDDC6C7EC06FC55C390D99A01BE5BEFCCD54C8D3B3A0E1380CFBE",
      "jetton": "0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE",
      "last_transaction_lt": "99750714000012",
      "code_hash": "iUaPAseOVwgC45l5yFFvw43wfqdqSDV+BTbyuns+43s=",
      "data_hash": "InbiibDqwhzppqxXoNBp6g4SL96w/p2UYXwzHuHrKMw="
    }
  ],
  "address_book": {
    "0:0000005CECBDC23E9FE415D530ADEE667EF35B4D3DB4CC49088B4F319179A86F": {
      "user_friendly": "EQAAAABc7L3CPp_kFdUwre5mfvNbTT20zEkIi08xkXmob5lS",
      "domain": null,
      "interfaces": [
        "jetton_wallet_governed"
      ]
    },
    "0:00000401C81EAEDED6DB1442376E806F91F285B11AC29D7101B684A9A457721F": {
      "user_friendly": "EQAAAAQByB6u3tbbFEI3boBvkfKFsRrCnXEBtoSppFdyH9n2",
      "domain": null,
      "interfaces": [
        "jetton_wallet_governed"
      ]
    },
    "0:3EABECA36F84A9D0BF45AEB25018BDD0C7501C26DAB4046C84EA4263BBCE9ADB": {
      "user_friendly": "UQA-q-yjb4Sp0L9FrrJQGL3Qx1AcJtq0BGyE6kJju86a2-at",
      "domain": null,
      "interfaces": [
        "wallet_v3r1"
      ]
    },
    "0:5E851231E85CDDC6C7EC06FC55C390D99A01BE5BEFCCD54C8D3B3A0E1380CFBE": {
      "user_friendly": "UQBehRIx6FzdxsfsBvxVw5DZmgG-W-_M1UyNOzoOE4DPviCG",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE": {
      "user_friendly": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
      "domain": null,
      "interfaces": [
        "jetton_master"
      ]
    }
  }
}
```
{% endcode %}
