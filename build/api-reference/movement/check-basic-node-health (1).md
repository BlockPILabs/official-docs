---
hidden: true
---

# Copy of Show some basic info of the node

<br>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/info

// Result
{
    "new_storage_format": false,
    "continuous_syncing_mode": "ExecuteTransactionsOrApplyOutputs",
    "bootstrapping_mode": "DownloadLatestStates",
    "internal_indexer_config": {
        "enable_transaction": false,
        "enable_event": false,
        "enable_event_v2_translation": false,
        "event_v2_translation_ignores_below_version": 0,
        "enable_statekeys": false,
        "batch_size": 10000
    }
}
```
{% endcode %}
