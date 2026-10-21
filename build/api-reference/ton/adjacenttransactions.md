# adjacenttransactions

Get the parent transaction, child transactions, or both for the specified transaction.

{% hint style="info" %}
Returns `404 adjacent transactions not found` when the transaction has no neighbours in the requested direction.
{% endhint %}

**Parameters**

* **`hash`** — string, optional. Transaction hash.
* **`direction`** — string, optional. Direction of the message relative to the transaction.

**Returns**

* `address_book` — object
* `transactions` — array of objects with fields `account`, `account_state_after`, `account_state_before`, `block_ref`, `description`, `emulated`, `end_status`, `finality`, `hash`, `in_msg`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/adjacentTransactions?hash=a30PDWY23%2B%2Bd6YkYp6C1Q%2Fn8XAdFudT%2BtvnywZjeNlw%3D&direction=both'

// Result
{
  "address_book": {
    "0:32081D54752B9340A75C777A94AF0483F07329DD296EB4F915BB45E477B93F8A": {
      "user_friendly": "EQAyCB1UdSuTQKdcd3qUrwSD8HMp3SlutPkVu0Xkd7k_itc5",
      "domain": null,
      "interfaces": [
        "jetton_wallet_governed"
      ]
    },
    "0:35F94592910A839F6977122D4DE04DCB0FB184BEC5F7BBE0889436B62AD99442": {
      "user_friendly": "EQA1-UWSkQqDn2l3Ei1N4E3LD7GEvsX3u-CIlDa2KtmUQkPd",
      "domain": null,
      "interfaces": [
        "jetton_wallet_governed"
      ]
    },
    "0:852443F8599FE6A5DA34FE43049AC4E0BEB3071BB2BFB56635EA9421287C283A": {
      "user_friendly": "EQCFJEP4WZ_mpdo0_kMEmsTgvrMHG7K_tWY16pQhKHwoOoy2",
      "domain": null,
      "interfaces": [
        "wallet_highload_v3r1"
      ]
    },
    "0:F785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78": {
      "user_friendly": "UQD3hWKePiaOHPOyLI3v2Z3rlIfl3JebkT7GewB_HC1eeP-y",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    }
  }
}
```
{% endcode %}
