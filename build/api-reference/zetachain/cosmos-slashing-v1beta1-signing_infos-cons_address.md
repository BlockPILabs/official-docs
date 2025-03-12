---
description: SigningInfo queries the signing info of given cons address
---

# /cosmos/slashing/v1beta1/signing\_infos/{cons\_address}

#### **Parameters:**

**cons\_address - string**, cons\_address is the address to query signing info of

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/slashing/v1beta1/signing_infos/zetavalcons1pnnh5ejzy6fpsh6wuld0cgfd9g3ffwawdc7l0h

// Result
{
  "val_signing_info": {
    "address": "zetavalcons1pnnh5ejzy6fpsh6wuld0cgfd9g3ffwawdc7l0h",
    "start_height": "0",
    "index_offset": "2083045",
    "jailed_until": "1970-01-01T00:00:00Z",
    "tombstoned": false,
    "missed_blocks_counter": "0"
  }
}
```
{% endcode %}
