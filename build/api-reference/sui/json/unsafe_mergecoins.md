---
description: Create an unsigned batched transaction.
---

# unsafe\_mergeCoins

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**primary\_coin< ObjectID >** -The coin object to merge into, this coin will remain after the transaction

**coin\_to\_merge< ObjectID >** - The coin object to be merged, this coin will be destroyed, the balance will be added to `primary_coin`

**gas< ObjectID >** - Gas object to be used in this transaction, node will pick one from the signer's possession if not provided&#x20;

**gas\_budget< BigInt\_for\_uint64 >** - The gas budget, the transaction will fail if the gas cost exceed the budget&#x20;

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
