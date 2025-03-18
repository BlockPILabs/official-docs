---
description: >-
  Retrieves account balance for coins / fungible asset (only for primary
  fungible asset store) for a given account, asset type and a specific ledger
  version.
hidden: true
---

# Copy of Get account balance​

The nodes prune account state history, via a configurable time window. If the requested ledger version has been pruned, the server responds with a 410.

#### **Path Parameters:**

**address**  string \<hex> required

Address of account with or without a `0x` prefix

**asset\_type** string \<hex> required

A hex encoded 32 byte Aptos account address or a struct tag.

This is represented in a string as a 64 character hex string, sometimes shortened by stripping leading 0s, and adding a 0x or Format: `{address}::{module name}::{struct name}`

#### Query Parameters：

**ledger\_version** string\<uint64>

Ledger version to get state of account. If not provided, it will be the latest version

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

integer uint64

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x21746fce17b3a44156107bdc483bfeabb0bc4a37b8ceabaff93ed454bdea9653/balance/0x1::aptos_coin::AptosCoin

// Result
1817122
```
{% endcode %}
