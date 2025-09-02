---
description: Return all Coin<coin_type> objects owned by an address.
---

# suix\_getCoins

#### **Parameters:**

**owner< SuiAddress >** - The owner's Sui address

**coin\_type< string >** - Optional type names for the coin (e.g., 0x168da5bf1f48dafc111b0a488fa454aca95e0b5e::usdc::USDC), default to 0x2::sui::SUI if not specified.

**cursor< ObjectID >** - Optional paging cursor

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
  "method": "suix_getCoins",
  "params": [
    "0x2b9839632975470cf865bcf5872d162c731ecb98f2453bb39679d0f0f9d1991e",
    "0x2::sui::SUI"
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
            }
        ],
        "nextCursor": "0x32785c9517896b8985a53ff047bac4e30380cb49b651f19fed26e770e132ac17",
        "hasNextPage": false
    },
    "id": 1
}
```
{% endcode %}
