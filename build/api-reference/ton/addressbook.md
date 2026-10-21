# addressbook

Query the address book for the specified addresses.

**Parameters**

* **`address`** — array of strings, required. List of addresses in any form to include in the address book. Maximum: 1024 addresses.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/addressBook?address=0%3AED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7'

// Result
{
  "0:ED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7": {
    "user_friendly": "EQDtFpEwcFAEcRe5mLVh2N6C0x-_hJEM7W61_JLnSF74p4q2",
    "domain": null,
    "interfaces": [
      "locker"
    ]
  }
}
```
{% endcode %}
