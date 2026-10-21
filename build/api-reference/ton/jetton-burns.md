# jetton burns

Query jetton burns that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`address`** — array of strings, optional. Address of the jetton wallet owner in any form. Maximum: 1000 addresses.
* **`jetton_wallet`** — array of strings, optional. Jetton wallet address in any form. Maximum: 1000 addresses.
* **`jetton_master`** — string, optional. Jetton master address in any form.
* **`start_utime`** — integer, optional. Query transactions with a generation timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query transactions with a generation timestamp at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query transactions where `lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query transactions where `lt` is at or below the specified value.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort transactions by `lt`.

**Returns**

* `address_book` — object
* `jetton_burns` — array of objects with fields `amount`, `custom_payload`, `decoded_custom_payload`, `jetton_master`, `jetton_wallet`, `owner`, `query_id`, `response_destination`, `trace_id`, `transaction_aborted`
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/jetton/burns?limit=2'

// Result
{
  "jetton_burns": [
    {
      "query_id": "0",
      "owner": "0:5F0CC5CD13EB9D29D19CE35F45D8DBD36FCA89C8E628FF7DA6089438141E8644",
      "jetton_wallet": "0:7FBD908EC5514A17A7063848B1A96C03EDA34400BA9ABEFD78E4E09F7176304D",
      "jetton_master": "0:BDF3FA8098D129B54B4F73B5BAC5D1E1FD91EB054169C3916DFC8CCD536D1000",
      "transaction_hash": "9cQPgzppGHpnt3XlJAN44wFvolmAliNAuErHBbdeUqQ=",
      "transaction_lt": "111332665000005",
      "transaction_now": 1792549976,
      "transaction_aborted": false,
      "amount": "5141426337",
      "response_destination": "0:5F0CC5CD13EB9D29D19CE35F45D8DBD36FCA89C8E628FF7DA6089438141E8644",
      "custom_payload": "te6cckEBAQEAAwAAAWAoXP0U",
      "decoded_custom_payload": null,
      "trace_id": "fbNDZxra04lIw/BecWbYdcgZA5Xnma9SHoSVoCkJcjs="
    }
  ],
  "address_book": {
    "0:351080EB477DF380BDB5AF00C87C6A3B8781135A279E9ED52F83B8C84FEDDA3F": {
      "user_friendly": "EQA1EIDrR33zgL21rwDIfGo7h4ETWieentUvg7jIT-3aP5GG",
      "domain": null,
      "interfaces": []
    },
    "0:3F2A977081938290416ADB1ADEE12E4B6C7B2BF0ABA5D2A5DF488E41D7EF57DE": {
      "user_friendly": "UQA_KpdwgZOCkEFq2xre4S5LbHsr8Kul0qXfSI5B1-9X3kyg",
      "domain": null,
      "interfaces": [
        "wallet_v5r1"
      ]
    },
    "0:54B8BCB42574C47675EA7D09430FCD5C86D84796A13516F47A0C6487318EED83": {
      "user_friendly": "EQBUuLy0JXTEdnXqfQlDD81chthHlqE1FvR6DGSHMY7tg1S0",
      "domain": null,
      "interfaces": []
    },
    "0:5F0CC5CD13EB9D29D19CE35F45D8DBD36FCA89C8E628FF7DA6089438141E8644": {
      "user_friendly": "UQBfDMXNE-udKdGc419F2NvTb8qJyOYo_32mCJQ4FB6GROv0",
      "domain": null,
      "interfaces": [
        "wallet_v5r1"
      ]
    },
    "0:7FBD908EC5514A17A7063848B1A96C03EDA34400BA9ABEFD78E4E09F7176304D": {
      "user_friendly": "EQB_vZCOxVFKF6cGOEixqWwD7aNEALqavv145OCfcXYwTezh",
      "domain": null,
      "interfaces": [
        "jetton_wallet"
      ]
    },
    "0:BDF3FA8098D129B54B4F73B5BAC5D1E1FD91EB054169C3916DFC8CCD536D1000": {
      "user_friendly": "EQC98_qAmNEptUtPc7W6xdHh_ZHrBUFpw5Ft_IzNU20QAJav",
      "domain": null,
      "interfaces": [
        "jetton_master"
      ]
    }
  }
}
```
{% endcode %}
