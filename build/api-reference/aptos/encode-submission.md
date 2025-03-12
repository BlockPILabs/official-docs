# Encode submission



This endpoint accepts an EncodeSubmissionRequest, which internally is a UserTransactionRequestInner (and optionally secondary signers) encoded as JSON, validates the request format, and then returns that request encoded in BCS. The client can then use this to create a transaction signature to be used in a SubmitTransactionRequest, which it then passes to the /transactions POST endpoint.

To be clear, this endpoint makes it possible to submit transaction requests to the API from languages that do not have library support for BCS. If you are using an SDK that has BCS support, such as the official Rust, TypeScript, or Python SDKs, you do not need to use this endpoint.

To sign a message using the response from this endpoint:

* Decode the hex encoded string in the response to bytes.
* Sign the bytes to create the signature.
* Use that as the signature field in something like Ed25519Signature, which you then use to build a TransactionSignature.

#### Request body：

Request to encode a submission

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

**secondary\_signers**  array\[string]

Secondary signer accounts of the request for Multi-agent

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

string\<hex>

All bytes (Vec) data is represented as hex-encoded string prefixed with `0x` and fulfilled with two hex digits per byte.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/transactions/encode_submission
--data
'{
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
  "secondary_signers": [
    "0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "
  ]
}'

// Result
{

}
```
{% endcode %}
