# ListOwnedObjects

#### **Parameters:**

**object\_type** - [string](https://docs.sui.io/references/fullnode-protocol#string) Optional type filter to limit the types of objects listed. Providing an object type with no type params will return objects of that type with any type parameter, e.g. `0x2::coin::Coin` will return all `Coin<T>` objects regardless of the type parameter `T`. Providing a type with a type param will retrict the returned objects to only those objects that match the provided type parameters, e.g. `0x2::coin::Coin<0x2::sui::SUI>` will only return `Coin<SUI>` objects.

**page\_size** - [uint32](https://docs.sui.io/references/fullnode-protocol#uint32) The maximum number of dynamic fields to return. The service may return fewer than this value. If unspecified, at most `50` entries will be returned. The maximum value is `1000`; values above `1000` will be coerced to `1000`.

**page\_token** - [bytes](https://docs.sui.io/references/fullnode-protocol#bytes) A page token, received from a previous `ListDynamicFields` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDynamicFields` must match the call that provided the page token.

**owner** - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The owner's Sui address.

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask)

#### **Returns:**

objects - [Object](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Object) Page of dynamic fields owned by the specified parent.

**next\_page\_token** - [bytes](https://docs.sui.io/references/fullnode-protocol#bytes) A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/live_data_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "owner": "0x0feb54a725aa357ff2f5bc6bb023c05b310285bd861275a30521f339a434ebb3"

}' 
sui.blockpi.network:443 sui.rpc.v2beta.LiveDataService/ListOwnedObjects
```
{% endcode %}
