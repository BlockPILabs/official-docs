# spotDeployState

#### Parameters

type: spotDeployState user: address (42-char hex)

#### Returns

Spot market deployment and auction state.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"spotDeployState","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
{"states":[],"gasAuction":{"startTimeSeconds":1785376800,"durationSeconds":111600,"startGas":"1000.0","currentGas":"873.40466397","endGas":null}}
```
{% endcode %}
