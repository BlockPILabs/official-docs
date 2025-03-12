# /getConsensusBlock

Get consensus block and its update timestamp.



**Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getConsensusBlock' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "consensus_block": 39984113,
    "timestamp": 1724744839.95082
  }
}
```
{% endcode %}
