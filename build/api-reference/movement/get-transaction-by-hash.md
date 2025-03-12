---
description: >-
  Look up a transaction by its hash. This is the same hash that is returned by
  the API when submitting a transaction
---

# Get transaction by hash



When given a transaction hash, the server first looks for the transaction in storage (on-chain, committed). If no on-chain transaction is found, it looks the transaction up by hash in the mempool (pending, not yet committed).

To create a transaction hash by yourself, do the following:

1. Hash message bytes: "RawTransaction" bytes + BCS bytes of Transaction.
2. Apply hash algorithm `SHA3-256` to the hash message bytes.
3. Hex-encode the hash bytes with `0x` prefix.

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
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/transactions/by_hash/0xce43e86741858d7c6722078a0bb32c633f37e4b9a79844fd6d661ea830e25148


// Result
{
    "version": "9",
    "hash": "0xce43e86741858d7c6722078a0bb32c633f37e4b9a79844fd6d661ea830e25148",
    "state_change_hash": "0xafb6e14fe47d850fd0a7395bcfb997ffacf4715e0f895cc162c218e4a7564bc6",
    "event_root_hash": "0x414343554d554c41544f525f504c414345484f4c4445525f4841534800000000",
    "state_checkpoint_hash": "0xbba9de2d2585214e0e5331cd7f66f2652cf8b2146465d67149344356de43c731",
    "gas_used": "0",
    "success": true,
    "vm_status": "Executed successfully",
    "accumulator_root_hash": "0xa8284e69faadc98f9893ac564e1d93b975b744869d9804a7454c2be4388c8d6a",
    "changes": [],
    "timestamp": "1732636319660843",
    "type": "state_checkpoint_transaction"
}
```
{% endcode %}
