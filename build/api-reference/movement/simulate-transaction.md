# Simulate transaction

The output of the transaction will have the exact transaction outputs and events that running an actual signed transaction would have. However, it will not have the associated state hashes, as they are not updated in storage. This can be used to estimate the maximum gas units for a submitted transaction.

To use this, you must:

* Create a SignedTransaction with a zero-padded signature.
* Submit a SubmitTransactionRequest containing a UserTransactionRequest containing that signature.

To use this endpoint with BCS, you must submit a SignedTransaction encoded as BCS. See SignedTransaction in types/src/transaction/mod.rs.

#### Query Parameters：：

**estimate\_gas\_unit\_price** boolean

If set to true, the gas unit price in the transaction will be ignored and the estimated value will be used

**estimate\_max\_gas\_amount** boolean

If set to true, the max gas value in the transaction will be ignored and the maximum possible gas will be used

**estimate\_prioritized\_gas\_unit\_price**  boolean

If set to true, the transaction will use a higher price than the original estimate.

#### Request body：

A request to submit a transaction

**sender** string\<hex> required

A hex encoded 32 byte Aptos account address.

**sequence\_number** string\<uint64> required

A string containing a 64-bit unsigned integer.

**max\_gas\_amount** string\<uint64> required

A string containing a 64-bit unsigned integer.

**gas\_unit\_price** string\<uint64> required

A string containing a 64-bit unsigned integer.

**expiration\_timestamp\_secs** string\<uint64> required

A string containing a 64-bit unsigned integer.

**payload** object required

Payload which runs a single entry function, or

Payload which runs a script that can run multiple functions, or

An enum of the possible transaction payloads

**signature** object required

A single Ed25519 signature, or

A Ed25519 multi-sig signature, or

Multi agent signature for multi agent transactions

#### **Response Header:**

**X-APTOS-BLOCK-HEIGHT** integer&#x20;

Current block height of the chain

**X-APTOS-CHAIN-ID** integer&#x20;

Chain ID of the current chain

**X-APTOS-EPOCH** integer&#x20;

Current epoch of the chain

**X-APTOS-LEDGER-OLDEST-VERSION** integer&#x20;

Oldest non-pruned ledger version of the chain

**X-APTOS-LEDGER-TIMESTAMPUSEC** integer&#x20;

Current timestamp of the chain

**X-APTOS-LEDGER-VERSION** integer&#x20;

Current ledger version of the chain

**X-APTOS-OLDEST-BLOCK-HEIGHT** integer&#x20;

Oldest non-pruned block height of the chain

#### **Response Body:**

Array

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/transactions/simulate
--data
{
  
}

// Result
{

}
```
{% endcode %}
