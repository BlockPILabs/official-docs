# GetObject

#### **Parameters:**

object\_id - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The `ObjectId` of the requested object.

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask) Mask specifying which fields to read. If no mask is specified, defaults to `object_id,version,digest`.

version - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64)  optional Request a specific version of the object. If no version is specified, and the object is live, then the latest version of the object is returned.

#### **Returns:**

**object** - [Object](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Object)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/ledger_service.proto 
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "object_id": "0x27c4fdb3b846aa3ae4a65ef5127a309aa3c1f466671471a806d8912a18b253e8",

}' 
sui.blockpi.network:443 sui.rpc.v2.LedgerService/GetObject
```
{% endcode %}
