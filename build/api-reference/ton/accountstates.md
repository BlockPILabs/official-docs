# accountstates

Query account states that match the specified filters.

**Parameters**

* **`address`** — array of strings, required. List of addresses in any form. Maximum: 1000 addresses.
* **`include_boc`** — boolean, optional, default `True`. Include code and data BoCs. Defaults to `true`.

**Returns**

* `accounts` — array of objects with fields `account_state_hash`, `address`, `balance`, `code_boc`, `code_hash`, `contract_methods`, `data_boc`, `data_hash`, `extra_currencies`, `frozen_hash`
* `address_book` — object
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/accountStates?address=0%3AED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7'

// Result
{
  "accounts": [
    {
      "address": "0:ED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7",
      "account_state_hash": "qSR45oV+iUejBShowo1Vhz1lfP1Za2z50PO5pjqF4Vw=",
      "balance": "1246187124150386674",
      "extra_currencies": {},
      "status": "active",
      "last_transaction_hash": "2On+zSO62+DjyNBNGJOkCYgtCs84pVcTpbNmCZGsFKA=",
      "last_transaction_lt": "111285831000019",
      "data_hash": "HpgtycjQc73Ff8WSKNazRBi+AJNzTd/PHboF/0jl/wM=",
      "code_hash": "gwyZpEfQl0222G7X2J/k8tLsIjWMtkKH4tMeVj695Uc=",
      "data_boc": "te6ccgECBgEAAQ8AAUKA5YQILcgsXJgD8ASdQrbkAGU1t4Bo6u+ABY/UAAAnjQABART/APSkE/S88sgLAgIBYgMEAZ7Q7aLt+zMx0NMDAXGwkVvgAdMfAvpA…",
      "code_boc": "te6ccgECEgEAAvUAART/APSkE/S88sgLAQIBYgIDA27QM9DTAwFxsJJfA+D6QDDbPALTHyGCENZBa/664wIBwADyvdMH0SDAZCHAdwLAclITsSKx8r4BEQQF…",
      "contract_methods": [
        0
      ],
      "interfaces": [
        "locker"
      ]
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
