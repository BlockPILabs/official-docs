---
description: Return the authentication key and the sequence number for an account address.
---

# Get account

#### **Path Parameters:**

**address  string** \<hex> required

Address of account with or without a `0x` prefix

#### Query Parameters：

**ledger\_version string**\<uint64>

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

Account data

A simplified version of the onchain Account resource

**sequence\_number** string\<uint64>

A string containing a 64-bit unsigned integer.

**authentication\_key** string

All bytes (Vec) data is represented as hex-encoded string prefixed with `0x` and fulfilled with two hex digits per byte.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/accounts/0xdb42353b3f77383dce21d9c55a9f6a51149b2a45d1f376def4d2ea43d1b7e399

// Result
{
    "sequence_number": "",
    "authentication_key": ""
}
```
{% endcode %}
