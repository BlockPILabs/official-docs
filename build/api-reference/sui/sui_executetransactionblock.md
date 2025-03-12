# sui\_executeTransactionBlock

Execute the transaction and wait for results if desired. Request types: 1. WaitForEffectsCert: waits for TransactionEffectsCert and then return to client. This mode is a proxy for transaction finality. 2. WaitForLocalExecution: waits for TransactionEffectsCert and make sure the node executed the transaction locally before returning the client. The local execution makes sure this node is aware of this transaction when client fires subsequent queries. However if the node fails to execute the transaction locally in a timely manner, a bool type in the response is set to false to indicated the case. request\_type is default to be `WaitForEffectsCert` unless options.show\_events or options.show\_effects is true

#### **Parameters:**

**tx\_bytes< Base64 >** - BCS serialized transaction data bytes without its type tag, as base-64 encoded string.

**signatures<\[ Base64 ]>** - A list of signatures (`flag || signature || pubkey` bytes, as base-64 encoded string). Signature is committed to the intent message of the transaction data, as base-64 encoded string.

**options< TransactionBlockResponseOptions >** - Options for specifying the content to be returned

**request\_type< ExecuteTransactionRequestType >** - The request type, derived from `SuiTransactionBlockResponseOptions` if None

#### **Returns:**

SuiTransactionBlockResponse< TransactionBlockResponse >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_executeTransactionBlock",
  "params": [
    "AAACACBqEB6aOvXIBwES+Ahkizbvv43uihqC3kbZUE6WoRCKFwEAjvdvVsOZYzousxC8qRJOXy84znOeqsu2YAaIgE4HhEgCAAAAAAAAACB9w3+ufZMpihJFwxtCBojBaGy00TVtFxgN2C6TpIPFqwEBAQEBAAEAAAS0l6kWtGVmCaf6gnoJGE1vR2gdO6dM4NejbGSysfiHAZ+Q9/hmzCnfsdpjc86U+dldylpA9OF2mRjuv5+64AvTAgAAAAAAAAAgjleHL0UiRGjh/BfIFHCJ3EMY/dQA22c2TvNQyVJnbYUEtJepFrRlZgmn+oJ6CRhNb0doHTunTODXo2xksrH4hwoAAAAAAAAAoIYBAAAAAAAA",
    [
      "AKD4XdltkCyBi1Heb4EJJ3lzuV3F4u7+CYeaE+Fd7qXpaT17yd4tHWjMf4CWq3TuXBLxTpkc2MV39P6p7eMV8QnqvbuA0Q1Bqu4RHV3JPpqmH+C527hWJGUBOZN1j9sg8w=="
    ],
    {
      "showInput": true,
      "showRawInput": true,
      "showEffects": true,
      "showEvents": true,
      "showObjectChanges": true,
      "showBalanceChanges": true,
      "showRawEffects": false
    },
    "WaitForLocalExecution"
  ]
}'

// Result

```
{% endcode %}
