# suix\_getOwnedObjects

Return the list of objects owned by an address. Note that if the address owns more than `QUERY_MAX_RESULT_LIMIT` objects, the pagination is not accurate, because previous page may have been updated when the next page is fetched. Please use suix\_queryObjects if this is a concern.

#### **Parameters:**

**address< SuiAddress >** - The owner's Sui address&#x20;

**query< ObjectResponseQuery >** - The objects query criteria.&#x20;

**cursor< ObjectID >** - An optional paging cursor. If provided, the query will start from the next item after the specified cursor. Default to start from the first item if not specified.&#x20;

**limit< uint >** - Max number of items returned per page, default to \[QUERY\_MAX\_RESULT\_LIMIT] if not specified.

#### **Returns:**

ObjectsPage< Page\_for\_SuiObjectResponse\_and\_ObjectID >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getOwnedObjects",
  "params": [
    "0xa69bb635dcee0f33643b4729ae81730d55e5e26860fac6839ce2d7ed7e6f29d2",
    {
      "filter": {
        "MatchAll": [
          {
            "StructType": "0x2::coin::Coin<0x2::sui::SUI>"
          },
          {
            "AddressOwner": "0xa69bb635dcee0f33643b4729ae81730d55e5e26860fac6839ce2d7ed7e6f29d2"
          },
          {
            "Version": "13488"
          }
        ]
      },
      "options": {
        "showType": true,
        "showOwner": true,
        "showPreviousTransaction": true,
        "showDisplay": false,
        "showContent": false,
        "showBcs": false,
        "showStorageRebate": false
      }
    },
    "0x76a1b4c23f2d9a9b6f0d8b2c17beace292b72aea16d6fb49b7d1ae51f33b01ed",
    3
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "data": [],
        "nextCursor": "0x76a1b4c23f2d9a9b6f0d8b2c17beace292b72aea16d6fb49b7d1ae51f33b01ed",
        "hasNextPage": false
    },
    "id": 1
}
```
{% endcode %}
