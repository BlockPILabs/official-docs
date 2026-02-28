# BatchGetObjects

#### **Parameters:**

**read\_mask** - Mask specifying which fields to read. If no mask is specified, defaults to `object_id,version,digest`.

**requests** - [GetObjectRequest](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-GetObjectRequest)

#### **Returns:**

**objects** - [GetObjectResult](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-GetObjectResult)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/ledger_service.proto 
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "object_id": "0x4897ec4008e4f6500880a547c25a6d4a26807c00ec359b4be24e6322fb2b86b5",
    "read_mask": {
        "paths": [
            "bcs",
            "object_id",
            "version",
            "digest",
            "contents",
            "owner",
            "object_type",
            "has_public_transfer",
            "previous_transaction"
        ]
    }
}' 
sui.blockpi.network:443 sui.rpc.v2beta.LedgerService/BatchGetObjects
```
{% endcode %}
