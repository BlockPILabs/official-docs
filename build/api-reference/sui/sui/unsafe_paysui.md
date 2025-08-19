# unsafe\_paySui

Send SUI coins to a list of addresses, following a list of amounts. This is for SUI coin only and does not require a separate gas coin object. Specifically, what pay\_sui does are: 1. debit each input\_coin to create new coin following the order of amounts and assign it to the corresponding recipient. 2. accumulate all residual SUI from input coins left and deposit all SUI to the first input coin, then use the first input coin as the gas coin object. 3. the balance of the first input coin after tx is sum(input\_coins) - sum(amounts) - actual\_gas\_cost 4. all other input coints other than the first one are deleted.

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**input\_coins<\[ ObjectID ]>** - The Sui coins to be used in this transaction, including the coin for gas payment.

**recipients<\[ SuiAddress ]>** - The recipients' addresses, the length of this vector must be the same as amounts.

**amounts<\[ BigInt\_for\_uint64 ]>** - The amounts to be transferred to recipients, following the same order

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
