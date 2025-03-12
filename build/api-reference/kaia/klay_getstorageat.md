---
description: Returns the value from a storage position at a given address.
---

# klay\_getStorageAt

#### **Parameters**

| Type                    | Description                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| 20-byte DATA            | Address of the storage.                                                                    |
| QUANTITY                | Integer of the position in the storage.                                                    |
| QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"` |

#### **Return Value**

| Type | Description                           |
| ---- | ------------------------------------- |
| DATA | The value at this storage position.s. |

#### Example

Calculating the correct position depends on the storage to retrieve. Consider the following contract deployed at `0x295a70b2de5e3953354a6a8344e616ed314d7251` by address `0x391694e7e0b0cce554cb130d723a9d27458f9298`.

{% code overflow="wrap" %}
```json
contract Storage {
    uint pos0;
    mapping(address => uint) pos1;

    function Storage() {
        pos0 = 1234;
        pos1[msg.sender] = 5678;
    }
}
```
{% endcode %}

Retrieving the value of `pos0` is straightforward:

{% code overflow="wrap" %}
```json
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method": "klay_getStorageAt", "params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x0", "latest"], "id": 1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

{"jsonrpc":"2.0","id":1,"result":"0x00000000000000000000000000000000000000000000000000000000000004d2"}
```
{% endcode %}

Retrieving an element of the map is harder. The position of an element in the map is calculated with:

{% code overflow="wrap" %}
```json
keccak(LeftPad32(key, 0), LeftPad32(map position, 0))
```
{% endcode %}

This means to retrieve the storage on `pos1["0x391694e7e0b0cce554cb130d723a9d27458f9298"]` we need to calculate the position with:

{% code overflow="wrap" %}
```json
keccak(decodeHex("000000000000000000000000391694e7e0b0cce554cb130d723a9d27458f9298" + "0000000000000000000000000000000000000000000000000000000000000001"))
```
{% endcode %}

The Klaytn console which comes with the `klay` library can be used to make the calculation

{% code overflow="wrap" %}
```json
> var key = "000000000000000000000000391694e7e0b0cce554cb130d723a9d27458f9298" + "0000000000000000000000000000000000000000000000000000000000000001"
undefined
> klay.sha3(key, {"encoding": "hex"})
"0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9"
```
{% endcode %}

Now to fetch the storage:

{% code overflow="wrap" %}
```json
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method": "klay_getStorageAt", "params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9", "latest"], "id": 1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

{"jsonrpc":"2.0","id":1,"result":"0x000000000000000000000000000000000000000000000000000000000000162e"}
```
{% endcode %}
