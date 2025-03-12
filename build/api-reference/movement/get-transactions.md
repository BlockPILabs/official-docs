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
