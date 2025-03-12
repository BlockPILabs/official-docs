---
description: Return all Coin objects owned by an address.
---

# suix\_getAllCoins

#### **Parameters:**

**owner< SuiAddress >** - The owner's Sui address\
**cursor< ObjectID >** - Optional paging cursor\
**limit< uint >** - Maximum number of items per page

#### **Returns:**

CoinPage< Page\_for\_Coin\_and\_ObjectID >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getAllCoins",
  "params": [
    "0x41f5975e3c6bd5c95f041a8493ad7e9934be26e69152d2c2e86d8a9bdbd242b3"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "data": [
            {
                "coinType": "0x2::sui::SUI",
                "coinObjectId": "0x32785c9517896b8985a53ff047bac4e30380cb49b651f19fed26e770e132ac17",
                "version": "225850805",
                "digest": "GYVqptpye6hUyA46LL9rEbH4P1DHLwR43xZNjxqU4yh8",
                "balance": "2957284",
                "previousTransaction": "8zFRf3y2n9dGLWBDz8JCGrgFN35Hi982hmpQzXWTgh7H"
            },
            ......
```
{% endcode %}
