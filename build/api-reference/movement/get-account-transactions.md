---
description: >-
  Retrieves transactions from an account. If the start version is too far in the
  past a 410 will be returned.  If no start version is given, it will start at 0
---

# Get account transactions

#### Path Parameters：

**address** string required

Address of account with or without a `0x` prefix

#### Query Parameters:

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
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/accounts/0xdb42353b3f77383dce21d9c55a9f6a51149b2a45d1f376def4d2ea43d1b7e399/transactions


// Result

```
{% endcode %}
