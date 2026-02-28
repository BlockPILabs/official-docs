# GetDatatype

#### **Parameters:**

string package\_id - Required. The `storage_id` of the requested package.&#x20;

string module\_name - Required. The name of the requested module.&#x20;

string name - Required. The name of the requested datatype.&#x20;

#### **Returns:**

datatype - The datatype.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/move_package_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
.....

}' 
sui.blockpi.network:443 sui.rpc.v2.MovePackageService/GetDatatype
```
{% endcode %}
