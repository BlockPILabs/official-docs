---
description: >-
  Same as /transactions/by_hash, but will wait for a pending transaction to be
  committed.
hidden: true
---

# Copy of Wait for transaction by hash​



To be used as a long poll optimization by clients, to reduce latency caused by polling. The "long" poll is generally a second or less but dictated by the server; the client must deal with the result as if the request was a normal /transactions/by\_hash request, e.g., by retrying if the transaction is pending.

#### Path Parameters：：

**txn\_hash** string required

Hash of transaction to retrieve

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

object

**Type** string

**Hash**  string

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
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/aptos/v1/your_api_key/v1/transactions/wait_by_hash/0x6fe169a36817e5b4225a1d878f6a8680f9a032cce180d1b8f4ddef9f0f045b6c

// Result

```
{% endcode %}
