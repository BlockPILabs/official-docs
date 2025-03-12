---
description: >-
  Create an unsigned transaction to send SUI coin object to a Sui address. The
  SUI object is also used as the gas object.
---

# unsafe\_transferSui

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**object\_id< ObjectID >** - The Sui coin object to be used in this transaction

**gas\_budget< BigInt\_for\_uint64 >** - The gas budget, the transaction will fail if the gas cost exceed the budget

**recipient< SuiAddress >** - The recipient's Sui address

**amount< BigInt\_for\_uint64 >** - The amount to be split out and transferred

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
