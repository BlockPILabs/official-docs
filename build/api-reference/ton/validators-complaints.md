# validators complaints

Return validator complaints that match the specified filters.

**Parameters**

* **`cycle_start`** — integer, optional. Validator cycle start time.
* **`election_id`** — integer, optional. Elector election ID.
* **`stake_holder_address`** — string, optional. Stakeholder address in any form.
* **`adnl_address`** — string, optional. ADNL address in hex, base64, or base64url form.
* **`validator_pubkey`** — string, optional. Validator public key in hex, base64, or base64url form.
* **`start_utime`** — integer, optional. Query complaints with `created_at` at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query complaints with `created_at` at or before the specified timestamp.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return.

**Returns**

* `address_book` — object
* `complaints` — array of objects with fields `adnl_addr`, `approved_percent`, `complaint_hash`, `created_at`, `cycle_start`, `description_boc`, `election_id`, `is_passed`, `paid`, `reward_address`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/validators/complaints?limit=2'

// Result
{
  "complaints": [
    {
      "cycle_start": 1785548552,
      "election_id": 1785548552,
      "complaint_hash": "A8dWJKBNmqobZCi8UCWQAXZ2Fx8Lsm57DLGmGgkc3vo=",
      "validator_pubkey": "D3FDB2144BFFF7E59C3A7EEAA1B5A5DF2165D629BBCA6C607BF31E418892C932",
      "adnl_addr": "710DF84CEAD31AC840922336AEFC2838C06A3EEE50CDA8EDD7EE2C4CA8345DB6",
      "stake_holder_address": "-1:C24EF58ECACC54E1E11AD2841BCAB8B58A2E16573D8F8DC1F3DA078C30278356",
      "description_boc": "te6cckEBCQEA+gACCMc3sMoBAgKiNGptTwgAAFVWtAhvBAT2BcZTy7tRA7B/AOmlZo5abqjC4D6aHdu8V+9bZ7W8wz6N2QWfdE/8+tkTEkXmD+MBiyPAV23O…",
      "created_at": 1785614106,
      "severity": 1,
      "reward_address": "-1:5B4CBD70C7CB4487E79D3447E33305A71F386803D7429DA6598B78149884CFE6",
      "paid": "1583277500",
      "suggested_fine": "101000000000",
      "suggested_fine_part": 0,
      "voted_validators": [
        {
          "validator_index": 48,
          "validator_pubkey": "20BBA02EA7EB43CDAC77D9EF3FFBE10662EB8E7FA9DB3ECF9632CBF511B6CA1B",
          "adnl_addr": "1AB49274FCC71907082EC5807984E832E5E132A2B88C0D93CFEF270BF3D1577C",
          "weight": "4577293150798045"
        }
      ],
      "vset_id": "3RBHpQV7CJjLl5BUHpvqcNBPWVHqZry8tkaxZS/QNBQ=",
      "weight_remaining": "358692304091210946",
      "approved_percent": 35.555,
      "is_passed": false
    }
  ],
  "address_book": {
    "-1:5B4CBD70C7CB4487E79D3447E33305A71F386803D7429DA6598B78149884CFE6": {
      "user_friendly": "Uf9bTL1wx8tEh-edNEfjMwWnHzhoA9dCnaZZi3gUmITP5jNV",
      "domain": null,
      "interfaces": [
        "wallet_v5r1"
      ]
    },
    "-1:A343527338F494F59EBF8E1C32BE4B529A46EC29D221EA5B6034FD111718A2BF": {
      "user_friendly": "Ef-jQ1JzOPSU9Z6_jhwyvktSmkbsKdIh6ltgNP0RFxiiv-0F",
      "domain": null,
      "interfaces": [
        "daolama_vault"
      ]
    },
    "-1:C24EF58ECACC54E1E11AD2841BCAB8B58A2E16573D8F8DC1F3DA078C30278356": {
      "user_friendly": "Ef_CTvWOysxU4eEa0oQbyri1ii4WVz2PjcHz2geMMCeDVv2S",
      "domain": null,
      "interfaces": [
        "daolama_vault"
      ]
    }
  }
}
```
{% endcode %}
