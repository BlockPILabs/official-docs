# sui\_devInspectTransactionBlock

Runs the transaction in dev-inspect mode. Which allows for nearly any transaction (or Move call) with any arguments. Detailed results are provided, including both the transaction effects and any return values.

#### **Parameters:**

**sender\_address< SuiAddress >** -&#x20;

**tx\_bytes< Base64 >** - BCS encoded TransactionKind(as opposed to TransactionData, which include gasBudget and gasPrice)&#x20;

**gas\_price< BigInt\_for\_uint64 >** - Gas is not charged, but gas usage is still calculated. Default to use reference gas price&#x20;

**epoch< BigInt\_for\_uint64 >** - The epoch to perform the call. Will be set from the system state object if not provided&#x20;

**additional\_args< DevInspectArgs >** - Additional arguments including gas\_budget, gas\_objects, gas\_sponsor and skip\_checks.

#### **Returns:**

evInspectResults< DevInspectResults >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_devInspectTransactionBlock",
  "params": [
    "0xd70420418b84502e506794227f897237764dde8d79a01ab2104bf742a277a2ab",
    "AAACACBnxtMcbJcOVn8D72fYEaT4Q2ZbjePygvpIs+AQO6m77QEAagYVO5/EhuEB8OnicDrIZm0GrsxN3355JqNhlwxlpbECAAAAAAAAACDoQ3EipycU+/EOvBcDPFtMkZiSbdzWAw3CwdmQCAtBWAEBAQEBAAEAAC9cVD1xauQ9RT3rOxmbva8bxwMMdoL4dwPc5DEkj+3gASxDgF0Nb1QCp60Npb3sVJx83qBrxKHTOaIlIe6pM7iJAgAAAAAAAAAgnvsgc1pPauyCE27/c+aBnHN3fSsxRAWdEJYzYFOryNAvXFQ9cWrkPUU96zsZm72vG8cDDHaC+HcD3OQxJI/t4AoAAAAAAAAAoIYBAAAAAAAA"
  ]
}'

// Result

```
{% endcode %}
