# GetTransaction

#### **Parameters:**

**read\_mask** - Mask specifying which fields to read. If no mask is specified, defaults to `object_id,version,digest`.

**digests** - [string](https://docs.sui.io/references/fullnode-protocol#string) The digests of the requested transactions.

#### **Returns:**

**transaction** -[ExecutedTransaction](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-ExecutedTransaction)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2beta2/ledger_service.proto 
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "digests": "6YVzczqTRTB88X1H5a4LGnKVTZoL7hfVDJ96DpHFU7Gy"
 
}' 
sui.blockpi.network sui.rpc.v2beta.LedgerService/GetTransaction
```
{% endcode %}
