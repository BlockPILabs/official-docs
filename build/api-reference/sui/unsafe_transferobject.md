---
description: >-
  Create an unsigned transaction to transfer an object from one address to
  another. The object's type must allow public transfers
---

# unsafe\_transferObject

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**object\_id< ObjectID >** - The ID of the object to be transferred

**gas< ObjectID >** - Gas object to be used in this transaction, node will pick one from the signer's possession if not provided

**gas\_budget< BigInt\_for\_uint64 >** - The gas budget, the transaction will fail if the gas cost exceed the budget

**recipient< SuiAddress >** - The recipient's Sui address

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
