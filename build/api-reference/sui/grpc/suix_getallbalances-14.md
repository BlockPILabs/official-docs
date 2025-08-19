# SubscribeCheckpoints

#### **Parameters:**

**read\_mask** - [FieldMask](https://docs.sui.io/references/fullnode-protocol#google-protobuf-FieldMask) Optional. Mask for specifiying which parts of the SubscribeCheckpointsResponse should be returned.

#### **Returns:**

**checkpoint** - [Checkpoint](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Checkpoint) The requested data for this checkpoint

**cursor** - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) Required. The checkpoint sequence number and value of the current cursor into the checkpoint stream

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2beta2/subscription_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
  

}' 
sui.blockpi.network sui.rpc.v2beta.SubscriptionService/SubscribeCheckpoints
```
{% endcode %}
