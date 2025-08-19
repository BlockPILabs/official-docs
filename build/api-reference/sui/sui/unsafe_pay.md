# unsafe\_pay

Send `Coin&lt;T>` to a list of addresses, where `T` can be any coin type, following a list of amounts, The object specified in the `gas` field will be used to pay the gas fee for the transaction. The gas object can not appear in `input_coins`. If the gas object is not specified, the RPC server will auto-select one.

#### **Parameters:**

**signer< SuiAddress >** - The transaction signer's Sui address&#x20;

**input\_coins<\[ ObjectID ]>** - The Sui coins to be used in this transaction&#x20;

**recipients<\[ SuiAddress ]>** - The recipients' addresses, the length of this vector must be the same as amounts.&#x20;

**amounts<\[ BigInt\_for\_uint64 ]>** - The amounts to be transferred to recipients, following the same order

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
