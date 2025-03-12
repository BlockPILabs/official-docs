# Maintenance windows

> The maintenance windows for a specific validator are future block height ranges in current epoch, in which the validator does not need produce block or chunk If the provided account is not a validator, then it will return the range from now to the end of the epoch.

* method: `EXPERIMENTAL_maintenance_windows`
* params:
  * `account_id`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://near.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "EXPERIMENTAL_maintenance_windows",
  "params": {
    "account_id": "node0"
  }
}'

// Result
{
    "jsonrpc": "2.0",
    "result": [
        [
            1028,
            1031
        ],
        [
            1034,
            1038
        ],
    ],
    "id": "dontcare"
}
```
{% endcode %}
