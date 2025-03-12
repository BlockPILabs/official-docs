# unsafe\_payAllSui

Send all SUI coins to one recipient. This is for SUI coin only and does not require a separate gas coin object. Specifically, what pay\_all\_sui does are: 1. accumulate all SUI from input coins and deposit all SUI to the first input coin 2. transfer the updated first coin to the recipient and also use this first coin as gas coin object. 3. the balance of the first input coin after tx is sum(input\_coins) - actual\_gas\_cost. 4. all other input coins other than the first are deleted.

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**input\_coins<\[ ObjectID ]>** - The Sui coins to be used in this transaction, including the coin for gas payment.

**recipients<\[ SuiAddress ]>** - The recipients' addresses

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
