---
description: >-
  By default this endpoint just checks that it can get the latest ledger info
  and then returns 200.
---

# Check basic node health

If the duration\_secs param is provided, this endpoint will return a 200 if the following condition is true:

`server_latest_ledger_info_timestamp >= server_current_time_timestamp - duration_secs`

#### **Path Parameters:**

None

#### Query Parameters：

**duration\_secs** integer

Threshold in seconds that the server can be behind to be considered healthy

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

Representation of a successful healthcheck

**message** string\


#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/-/healthy

// Result
{
    "message": "aptos-node:ok"
}
```
{% endcode %}
