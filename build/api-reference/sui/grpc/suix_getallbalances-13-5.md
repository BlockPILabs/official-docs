# LookupName

#### **Parameters:**

string name -  Required. The SuiNS name to lookup. Supports both `@name` as well as `name.sui` formats.

#### **Returns:**

record - The record for the requested name

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/name_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
 .....

}' 
sui.blockpi.network:443 sui.rpc.v2.NameService/LookupName
```
{% endcode %}
