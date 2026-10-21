# addressinformation

Get smart contract information for the specified account.

**Parameters**

* **`address`** — string, required. Account address in any form.
* **`use_v2`** — boolean, optional, default `True`. Use the API v2 method. This option is not recommended.

**Returns**

* `balance` — string
* `code` — string
* `data` — string
* `frozen_hash` — string
* `last_transaction_hash` — string
* `last_transaction_lt` — string
* `status` — string
* `suspended` — boolean

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/addressInformation?address=EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs'

// Result
{
  "balance": "1071874966975",
  "code": "te6ccgECGAEABbsAART/APSkE/S88sgLAQIBYgIDAgLLBAUCASAUFQLz0MtDTAwFxsI47MIAg1yHTHwGCEBeNRRm6kTDhgEDXIfoAMO1E0PoA+kD6QNTU0VB…",
  "data": "te6ccgEBBAEAdQACU3BRSOO6q8sIAMiB/HjSggcHLHKKLniWIo834XNprhIcsO73tLA4XzMwQAECCEICj0Utek39dAZraCNlF3JZ7QVzRDW+drX9S9XYryt8…",
  "last_transaction_lt": "111307519000025",
  "last_transaction_hash": "e+pO3/W7/FQpk0qitOvPATwf/AFsmUn7YGVAmEAGnIg=",
  "frozen_hash": null,
  "status": "active"
}
```
{% endcode %}
