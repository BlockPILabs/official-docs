---
description: >-
  Create an unsigned transaction to split a coin object into multiple equal-size
  coins.
---

# unsafe\_splitCoinEqual

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**coin\_object\_id< ObjectID >** - The coin object to be spilt&#x20;

**split\_amounts<\[ BigInt\_for\_uint64 ]>** - The amounts to split out from the coin

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
