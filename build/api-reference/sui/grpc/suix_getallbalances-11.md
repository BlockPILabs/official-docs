# ListDynamicFields

#### **Parameters:**

**page\_size** - [uint32](https://docs.sui.io/references/fullnode-protocol#uint32) The maximum number of dynamic fields to return. The service may return fewer than this value. If unspecified, at most `50` entries will be returned. The maximum value is `1000`; values above `1000` will be coerced to `1000`.

**page\_token** - [bytes](https://docs.sui.io/references/fullnode-protocol#bytes) A page token, received from a previous `ListDynamicFields` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDynamicFields` must match the call that provided the page token.

**parent** - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The `UID` of the parent, which owns the collections of dynamic fields.

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask)

#### **Returns:**

**dynamic\_fields** - [DynamicField](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-DynamicField) Page of dynamic fields owned by the specified parent.

**next\_page\_token** - [bytes](https://docs.sui.io/references/fullnode-protocol#bytes) A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/state_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "parent": "0x0feb54a725aa357ff2f5bc6bb023c05b310285bd861275a30521f339a434ebb3"

}' 
sui.blockpi.network:443 sui.rpc.v2.StateService/ListDynamicFields
```
{% endcode %}
