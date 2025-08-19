# sui\_getLoadedChildObjects

#### **Parameters:**

**digest< TransactionDigest >**

#### **Returns:**

SuiLoadedChildObjectsResponse< LoadedChildObjectsResponse >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getLoadedChildObjects",
  "params": [
    "6hpz6Qxv6t5VkNT5rcBKQS2Jootr6WHuSuRMLmmN13Jg"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "loadedChildObjects": []
    },
    "id": 1
}
```
{% endcode %}
