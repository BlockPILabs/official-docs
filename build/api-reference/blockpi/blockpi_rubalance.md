---
description: >-
  Using any existing key to query the currently RU balance of the account which
  owns the api key.
---

# blockpi\_ruBalance

{% hint style="info" %}
This method is to use any existing key to check the RU balance of your account, no matter how many keys in the account. The key is the last 40 digits of an private endpoint.&#x20;
{% endhint %}

For example, a user created 4 private endpoints and his remaining RU is 99M .

> _1) https://polygon-zkevm.blockpi.network/v1/rpc/**60794194a000ijb35af7e1180i311a26297a3b0w**_
>
> _2) https://arbitrum-nova.blockpi.network/v1/rpc/**1ee7d16c79ada6612ebf0q745fda72f57e593bd8**_
>
> _3) https://klaytn.blockpi.network/v1/rpc/**c338e93b14dc913700369e6c58d3184405ff7b1cb**_
>
> _4) https://polygon-zkevm.blockpi.network/v1/rpc/**4e322aee2acbba725782361y6fa64afc20706107**_

Using _**4e322aee2acbba725782361y6fa64afc20706107**_ or _**c338e93b14dc913700369e6c58d3184405ff7b1cb**_ as the parameter will give the same response of the 99M remaining RU.&#x20;

***

#### **Parameters:**

**apikey** -- any API key that the users already created in their account.

#### **Returns:**

**balance** -- the remaining RU balance of the account.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl  https://api.blockpi.io/openapi/v1/rpc -X POST -H "Content-Type: application/json" 
--data '{
    "jsonrpc": "2.0",
    "method": "blockpi_ruBalance",
    "params": [
        {
            "apiKey": "60794194a000ijb35af7e1180i311a26297a3b0w" 
        }
    ],
    "id": 1
}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "balance": 0
    }
}
```
{% endcode %}
