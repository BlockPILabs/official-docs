---
description: Create an unsigned batched transaction.
---

# unsafe\_batchTransaction

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**single\_transaction\_params<\[ RPCTransactionRequestParams ]>** - List of transaction request parameters&#x20;

**gas< ObjectID >** - Gas object to be used in this transaction, node will pick one from the signer's possession if not provided&#x20;

**gas\_budget< BigInt\_for\_uint64 >** - The gas budget, the transaction will fail if the gas cost exceed the budget&#x20;

**txn\_builder\_mode< SuiTransactionBlockBuilderMode >** - Whether this is a regular transaction or a Dev Inspect Transaction

#### **Returns:**

TransactionBlockBytes< TransactionBlockBytes >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'<as described above>'

// Result

```
{% endcode %}
