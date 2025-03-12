---
description: Params queries all parameters of the ICA controller submodule.
---

# /ibc/apps/interchain\_accounts/controller/v1/params

#### **Parameters:**

body - object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/apps/interchain_accounts/controller/v1/params

// Result
{
    "code": 2,
    "message": "value method github.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/controller/keeper.Keeper.Params called using nil *Keeper pointer: panic",
    "details": []
}
```
{% endcode %}
