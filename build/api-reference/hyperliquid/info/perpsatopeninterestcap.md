# perpsAtOpenInterestCap

#### Parameters

type: perpsAtOpenInterestCap

#### Returns

List of perpetuals currently at their open interest cap.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"perpsAtOpenInterestCap"}'

// Result
["CANTO","FTM","JELLY","LOOM","RLB","SAGA","ZEREBRO"]
```
{% endcode %}
