---
description: AccountAddressByID returns account address based on account number.
---

# /cosmos/auth/v1beta1/address\_by\_id/{id}

#### **Parameters:**

**id-string**，id is the account number of the address to be queried.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/address_by_id/0

// Result
{
  "account_address": "zeta18wqarvdsvm3sdq86xf4mlnev0wqtvcgg4vnl95"
}
```
{% endcode %}
