# spotMeta

#### Parameters

| Name | Type   | Required | Description  |
| ---- | ------ | -------- | ------------ |
| type | String | Yes      | `"spotMeta"` |

#### Returns

**Object** - Contains `tokens` (array of token info) and `universe` (array of spot pair configs).

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"spotMeta"}'

// Result
{"universe":[{"tokens":[1,0],"name":"PURR/USDC","index":0,"isCanonical":true},{"tokens":[2,0],"name":"@1","index":1,"isCanonical":false},{"tokens":[3,0],"name":"@2","index":2,"isCanonical":false},{"tokens":[4,0],"name":"@3","index":3,"isCanonical":false},{"tokens":[5,0],"name":"@4","index":4,"isCanonical":false},{"tokens":[6,0],"name":"@5","index":5,"isCanonical":false},{"tokens":[7,0],"name":"@6","index":6,"isCanonical":false},{"tokens":[8,0],"name":"@7","index":7,"isCanonical":false},{"tokens":[9,0],"name":"@8","index":8,"isCanonical":false},{"tokens":[10,0],"name":"@9","index":9,"isCanonical":false},{"tokens":[11,0],"name":"@10","index":10,"isCanonical":false},{"tokens":[12,0],"name":"@11","index":11,"isCanonical":false},{"tokens":[13,0],"name":"@12","index":12,"isCanonical":false},{"tokens":[14,0],"name":"@13","index":13,"isCanonical":false},{"tokens":[15,0],"name":"@14","index":14,"isCanonical":false},{"tokens":[16,0],"name":"@15","index":15,"isCanonical":false},{"tokens":[17,0],"
  ...
```
{% endcode %}
