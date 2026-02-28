# GetCheckpoint

#### **Parameters:**

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask) Mask specifying which fields to read. If no mask is specified, defaults to `object_id,version,digest`.

**digests** - [string](https://docs.sui.io/references/fullnode-protocol#string) Required. The digest of the requested checkpoint.

or\
**sequence\_number** - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) The sequence number of the requested checkpoint.

#### **Returns:**

**checkpoint** - [Checkpoint](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Checkpoint)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/ledger_service.proto 
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{

}' 
sui.blockpi.network:443 sui.rpc.v2.LedgerService/GetCheckpoint
```
{% endcode %}
