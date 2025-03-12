# eth\_mining

#### **Parameters:**

none

#### **Returns:**

**Boolean**- true if the node is mining, otherwise false.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_mining","params":[],"id":67}'

// Result
{
    "jsonrpc":"2.0",
    "id":67,
    "result":false
}
```
{% endcode %}
