# ReverseLookupName

#### **Parameters:**

string address -  Required. The address to perform a reverse lookup for.

#### **Returns:**

record - The record for the SuiNS name linked to the requested address

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/name_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
 .....

}' 
sui.blockpi.network:443 sui.rpc.v2.NameService/ReverseLookupName
```
{% endcode %}
