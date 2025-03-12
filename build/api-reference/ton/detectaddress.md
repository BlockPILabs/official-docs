# /detectAddress

Get all possible address forms.



**Parameters:**

**address - string,** Identifier of target TON account in any form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/detectAddress?address=EQCgH4od_xrY2pviA7MI30zdKG6z-7d2mh79Ki4GRVwRfHXM' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "raw_form": "0:a01f8a1dff1ad8da9be203b308df4cdd286eb3fbb7769a1efd2a2e06455c117c",
    "bounceable": {
      "b64": "EQCgH4od/xrY2pviA7MI30zdKG6z+7d2mh79Ki4GRVwRfHXM",
      "b64url": "EQCgH4od_xrY2pviA7MI30zdKG6z-7d2mh79Ki4GRVwRfHXM"
    },
    "non_bounceable": {
      "b64": "UQCgH4od/xrY2pviA7MI30zdKG6z+7d2mh79Ki4GRVwRfCgJ",
      "b64url": "UQCgH4od_xrY2pviA7MI30zdKG6z-7d2mh79Ki4GRVwRfCgJ"
    },
    "given_type": "friendly_bounceable",
    "test_only": false
  }
}
```
{% endcode %}
