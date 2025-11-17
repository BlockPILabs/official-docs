# ListBalances

#### **Parameters:**

**owner** - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The owner's Sui address.

**page\_size** - [uint32](https://docs.sui.io/references/fullnode-protocol#uint32) The maximum number of balance entries to return. The service may return fewer than this value. If unspecified, at most `50` entries will be returned. The maximum value is `1000`; values above `1000` will be coerced to `1000`.

**page\_token** - [bytes](https://docs.sui.io/references/fullnode-protocol#bytes) A page token, received from a previous `ListBalances` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBalances` must match the call that provided the page token.

#### **Returns:**

**balances** - [Balance](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Balance) The list of coin types and their respective balances.

**next\_page\_token** - [bytes](https://docs.sui.io/references/fullnode-protocol#bytes) A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2beta2/live_data_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "owner": "0x0feb54a725aa357ff2f5bc6bb023c05b310285bd861275a30521f339a434ebb3"

}' 
sui.blockpi.network:443 sui.rpc.v2beta.LiveDataService/ListBalances
```
{% endcode %}
