# GetEpoch

#### **Parameters:**

**epoch**- [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) The requested epoch. If no epoch is provided the current epoch will be returned.

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask) Mask specifying which fields to read. If no mask is specified, defaults to `object_id,version,digest`.

#### **Returns:**

**epoch** - [Epoch](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Epoch)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/ledger_service.proto 
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "digests": "6YVzczqTRTB88X1H5a4LGnKVTZoL7hfVDJ96DpHFU7Gy",
    "read_mask": {
        
    }
}' 
sui.blockpi.network:443 sui.rpc.v2beta.LedgerService/GetEpoch
```
{% endcode %}
