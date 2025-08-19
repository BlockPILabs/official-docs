# GetBalance

#### **Parameters:**

**coin\_type** - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The type names for the coin (e.g., 0x2::sui::SUI).

**owner** - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The owner's Sui address.

#### **Returns:**

**balance** - [Balance](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Balance) The balance information for the requested coin type.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2beta2/live_data_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "owner": "0x0feb54a725aa357ff2f5bc6bb023c05b310285bd861275a30521f339a434ebb3",
    "coin_type": "0x2::sui::SUI"

}' 
sui.blockpi.network sui.rpc.v2beta.LiveDataService/GetBalance
```
{% endcode %}
