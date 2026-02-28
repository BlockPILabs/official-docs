# GetCoinInfo

#### **Parameters:**

coin\_type - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The coin type to request information about

#### **Returns:**

coin\_type - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The coin type.

metadata - [CoinMetadata](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-CoinMetadata) This field will be populated with information about this coin type's `0x2::coin::CoinMetadata` if it exists and has not been wrapped.

regulated\_metadata - [RegulatedCoinMetadata](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-RegulatedCoinMetadata) If this coin type is a regulated coin, this field will be populated with information about its `0x2::coin::RegulatedCoinMetadata` object.

treasury - [CoinTreasury](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-CoinTreasury) This field will be populated with information about this coin type's `0x2::coin::TreasuryCap` if it exists and has not been wrapped.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/state_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "coin_type": "0x2::sui::SUI"

}' 
sui.blockpi.network:443 sui.rpc.v2.StateService/GetCoinInfo
```
{% endcode %}
