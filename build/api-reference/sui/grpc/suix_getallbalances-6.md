# GetServiceInfo

#### **Parameters:**

**None**

#### **Returns:**

**chain** - [string](https://docs.sui.io/references/fullnode-protocol#string) Human-readable name of the chain that this node is on. This is intended to be a human-readable name like `mainnet`, `testnet`, and so on.

**chain\_id** - [string](https://docs.sui.io/references/fullnode-protocol#string) The chain identifier of the chain that this node is on. The chain identifier is the digest of the genesis checkpoint, the checkpoint with sequence number 0.

**checkpoint\_height** - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) Checkpoint height of the most recently executed checkpoint.

**epoch** - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) Current epoch of the node based on its highest executed checkpoint.

**lowest\_available\_checkpoint** - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) The lowest checkpoint for which checkpoints and transaction data are available.

**lowest\_available\_checkpoint\_objects** - [uint64](https://docs.sui.io/references/fullnode-protocol#uint64) The lowest checkpoint for which object data is available.

**server** - [string](https://docs.sui.io/references/fullnode-protocol#string) Software version of the service. Similar to the `server` http header.

**timestamp** - [Timestamp](https://docs.sui.io/references/fullnode-protocol#google-protobuf-Timestamp) Unix timestamp of the most recently executed checkpoint.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/ledger_service.proto 
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
   

}' 
sui.blockpi.network:443 sui.rpc.v2.LedgerService/GetServiceInfo
```
{% endcode %}
