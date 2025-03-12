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
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6

// Result
{
    "sequence_number": "45294",
    "authentication_key": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6"
}
```
{% endcode %}
