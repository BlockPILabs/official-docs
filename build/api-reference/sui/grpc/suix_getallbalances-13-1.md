# GetPackage

#### **Parameters:**

string package\_id - Required. The `storage_id` of the requested package.&#x20;

#### **Returns:**

Package package - The package.<br>

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/move_package_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
.....
}' 
sui.blockpi.network:443 sui.rpc.v2.MovePackageService/GetPackage
```
{% endcode %}
