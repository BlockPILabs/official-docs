# validators events

Return validator stake acceptance, rejection, and recovery events.

**Parameters**

* **`stake_holder_address`** — string, optional. Stakeholder address in any form.
* **`adnl_address`** — string, optional. ADNL address in hex, base64, or base64url form.
* **`validator_pubkey`** — string, optional. Validator public key in hex, base64, or base64url form.
* **`type`** — string, optional. Filter by event type: `stake_accepted`, `stake_rejected`, or `stake_recovered`.
* **`start_utime`** — integer, optional. Query events with a timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query events with a timestamp at or before the specified timestamp.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return.

**Returns**

* `address_book` — object
* `end_utime` — integer
* `events` — array of objects with fields `adnl_addr`, `amount`, `election_id`, `query_id`, `reason`, `stake_holder_address`, `tx_hash`, `tx_lt`, `type`, `utime`
* `start_utime` — integer

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/validators/events?limit=2'

// Result
{
  "events": [
    {
      "tx_hash": "Wi8iCDgKaxKh1AsugmWAaIx8B65HrvHijNZra9JR2gc=",
      "tx_lt": "111296992000003",
      "utime": 1792535714,
      "type": "stake_accepted",
      "stake_holder_address": "-1:F7B79A8F9EE9AB6EB0B08DFE533AF79DDC4C428638D05DD0F83C5963B6E3F63F",
      "validator_pubkey": "85953B1D6D5BCAAF2AE910990CBA6E904127CADEDB3A24CCA9DA79A647500238",
      "adnl_addr": "4DBBE6690869600B371547EAC20F0F577E1446B02CE35F45C6064E2DEA643AAA",
      "election_id": 1792560904,
      "query_id": "1792535713269",
      "amount": "2877502820855702"
    }
  ],
  "address_book": {
    "-1:F7B79A8F9EE9AB6EB0B08DFE533AF79DDC4C428638D05DD0F83C5963B6E3F63F": {
      "user_friendly": "Ef_3t5qPnumrbrCwjf5TOved3ExChjjQXdD4PFljtuP2PxTW",
      "domain": null,
      "interfaces": null
    }
  }
}
```
{% endcode %}
