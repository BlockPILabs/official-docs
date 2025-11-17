# SimulateTransaction

#### **Parameters:**

**checks** - [TransactionChecks](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-SimulateTransactionRequest-TransactionChecks) Specify whether checks should be ENABLED (default) or DISABLED while executing the transaction

**do\_gas\_selection** - [bool](https://docs.sui.io/references/fullnode-protocol#bool) Perform gas selection based on a budget estimation and include the selected gas payment and budget in the response. This option will be ignored if `checks` is `DISABLED`.

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask)

**transaction** - [Transaction](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Transaction)

#### **Returns:**

**outputs** - [CommandResult](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-CommandResult)

**transaction** - [ExecutedTransaction](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-ExecutedTransaction)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2beta2/live_data_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
    "transaction": [ ... ]

}' 
sui.blockpi.network:443 sui.rpc.v2beta.LiveDataService/SimulateTransaction
```
{% endcode %}
