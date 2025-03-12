# klay\_isSenderTxHashIndexingEnabled

Returns `true` if the node is indexing sender transaction hash to transaction hash mapping information. It is disabled by default and can be enabled by `--sendertxhashindexing`.

#### **Parameters**

None

#### **Return Value**

| Type    | Description                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------- |
| Boolean | `true` means the node is indexing sender transaction hash to transaction hash mapping information. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_isSenderTxHashIndexingEnabled","id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```
{% endcode %}
