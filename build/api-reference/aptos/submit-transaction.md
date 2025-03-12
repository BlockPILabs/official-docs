---
description: >-
  Retrieve on-chain committed transactions. The page size and start ledger
  version can be provided to get a specific sequence of transactions.
---

# Submit transaction

This endpoint accepts transaction submissions in two formats.

To submit a transaction as JSON, you must submit a SubmitTransactionRequest. To build this request, do the following:

1. Encode the transaction as BCS. If you are using a language that has

native BCS support, make sure of that library. If not, you may take advantage of /transactions/encode\_submission. When using this endpoint, make sure you trust the node you're talking to, as it is possible they could manipulate your request. 2. Sign the encoded transaction and use it to create a TransactionSignature. 3. Submit the request. Make sure to use the "application/json" Content-Type.

To submit a transaction as BCS, you must submit a SignedTransaction encoded as BCS. See SignedTransaction in types/src/transaction/mod.rs. Make sure to use the `application/x.aptos.signed_transaction+bcs` Content-Type.

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

A transaction waiting in mempool

**hash** string

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

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/transactions
--data
{
  "sender": "0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 ",
  "sequence_number": "32425224034",
  "max_gas_amount": "32425224034",
  "gas_unit_price": "32425224034",
  "expiration_timestamp_secs": "32425224034",
  "payload": {
    "type": "entry_function_payload",
    "function": "0x1::aptos_coin::transfer",
    "type_arguments": [
      "string"
    ],
    "arguments": [
      null
    ]
  },
  "signature": {
    "type": "ed25519_signature",
    "public_key": "0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 ",
    "signature": "0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "
  }
}

// Result
{

}
```
{% endcode %}
