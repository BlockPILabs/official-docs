---
description: Create an unsigned transaction to publish a Move package.
---

# unsafe\_publish

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**compiled\_modules<\[ Base64 ]>** - The compiled bytes of a Move package&#x20;

**dependencies<\[ ObjectID ]>** - A list of transitive dependency addresses that this set of modules depends on.&#x20;

**gas< ObjectID >** - Gas object to be used in this transaction, node will pick one from the signer's possession if not provided

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
