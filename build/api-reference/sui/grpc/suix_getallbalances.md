# ExecuteTransaction

#### **Parameters:**

**read\_mask** - Mask specifying which fields to read. If no mask is specified, defaults to finality.

**signatures** - Set of UserSigantures authorizing the execution of the provided transaction

**transaction** - The transaction to execute.

#### **Returns:**

finality - Indicates the finality of the executed transaction.

transaction - object of [ExecutedTransaction](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-ExecutedTransaction)

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/transaction_execution_service.proto 
-H "x-token: YOUR_TOKEN_VALUE"
-d '{
    "transaction": { ...  },
    "options": {
      "show_input": true,
      "show_effects": true,
      "show_events": true,
      "show_object_changes": true,
      "show_balance_changes": true
  }
}' 
sui.blockpi.network:443 sui.rpc.v2beta.LedgerService/ExecuteTransaction
```
{% endcode %}
