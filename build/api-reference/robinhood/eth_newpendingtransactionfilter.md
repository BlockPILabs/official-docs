# eth\_newpendingtransactionfilter

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - A filter id.

Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call [eth\_getFilterChanges](/broken/pages/c465f0be1bc7256c68335dcc852b589518233b9d).

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x4ff5a315a69f36b9a072e69e7227020d"
}
```
{% endcode %}
