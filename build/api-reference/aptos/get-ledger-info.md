---
description: >-
  Get the latest ledger information, including data such as chain ID, role type,
  ledger versions, epoch, etc.
---

# Get ledger info

If the duration\_secs param is provided, this endpoint will return a 200 if the following condition is true:

`server_latest_ledger_info_timestamp >= server_current_time_timestamp - duration_secs`

#### **Path Parameters:**

None

#### Query Parameters：

None

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

The struct holding all data returned to the client by the index endpoint (i.e., GET "/"). Only for responding in JSON

**chain\_id** integer&#x20;

Chain ID of the current chain

**epoch** string\<uint64>

A string containing a 64-bit unsigned integer.

**ledger\_version** string\<uint64>

A string containing a 64-bit unsigned integer.

**oldest\_ledger\_version** string\<uint64>

A string containing a 64-bit unsigned integer.

**ledger\_timestamp** string\<uint64>

A string containing a 64-bit unsigned integer.

**node\_role** string&#x20;

Allowed values: validator full\_node

**oldest\_block\_height** string\<uint64>

A string containing a 64-bit unsigned integer.

**block\_height** string\<uint64>

A string containing a 64-bit unsigned integer.

**git\_hash** string\


#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/

// Result
{
    "chain_id": 1,
    "epoch": "487",
    "ledger_version": "36258508",
    "oldest_ledger_version": "0",
    "ledger_timestamp": "1669096800308226",
    "node_role": "full_node",
    "oldest_block_height": "0",
    "block_height": "11667199",
    "git_hash": "3b12b747b53a0dc610b0ea960459bb834a940852"
}
```
{% endcode %}
