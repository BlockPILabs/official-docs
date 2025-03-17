---
description: >-
  Retrieve on-chain committed transactions. The page size and start ledger
  version can be provided to get a specific sequence of transactions.
---

# Get transactions

If the version has been pruned, then a 410 will be returned.

To retrieve a pending transaction, use /transactions/by\_hash.

#### Query Parameters：

**limit** integer

Max number of transactions to retrieve. If not provided, defaults to default page size

**start** string\<uint64>

Ledger version to start list of transactions. If not provided, defaults to showing the latest transactions

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

array

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/transactions?limit=1

// Result
{
    "version": "523370",
    "hash": "0x820800ad38ff5f746890c1e22e7b4a3a4a023e95b17a5e11b34617d157b436b3",
    "state_change_hash": "0xafb6e14fe47d850fd0a7395bcfb997ffacf4715e0f895cc162c218e4a7564bc6",
    "event_root_hash": "0x414343554d554c41544f525f504c414345484f4c4445525f4841534800000000",
    "state_checkpoint_hash": "0x7a3c1c0abdb64b6c2a0f35b15075c2a9f84881bb5bd465f543d7c7b1cdeb8352",
    "gas_used": "0",
    "success": true,
    "vm_status": "Executed successfully",
    "accumulator_root_hash": "0x65f2e2a6be1f9435712661321794f9251722287905cb27b5dc20a39daa4d5d2a",
    "changes": [],
    "timestamp": "1742195401470227",
    "type": "state_checkpoint_transaction"
}
```
{% endcode %}
