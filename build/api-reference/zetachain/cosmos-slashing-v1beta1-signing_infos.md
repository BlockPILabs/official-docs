---
description: SigningInfos queries signing info of all validators
---

# /cosmos/slashing/v1beta1/signing\_infos

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/slashing/v1beta1/signing_infos

// Result
{
  "info": [
    {
      "address": "zetavalcons1pnnh5ejzy6fpsh6wuld0cgfd9g3ffwawdc7l0h",
      "start_height": "0",
      "index_offset": "2083033",
      "jailed_until": "1970-01-01T00:00:00Z",
      "tombstoned": false,
      "missed_blocks_counter": "0"
    },
    {
      "address": "zetavalcons195n5lay8qdpn534dd7kkxmsrg7m6mslc30aujp",
      "start_height": "1838669",
      "index_offset": "244363",
      "jailed_until": "1970-01-01T00:00:00Z",
      "tombstoned": false,
      "missed_blocks_counter": "0"
    },
    {
      "address": "zetavalcons1fhz9lcg36z950r4xemz9mey0nwym80mzaf9xzq",
      "start_height": "0",
      "index_offset": "2083033",
      "jailed_until": "1970-01-01T00:00:00Z",
      "tombstoned": false,
      "missed_blocks_counter": "0"
    },
    {
      "address": "zetavalcons10wss22veykvr96jaydl9dkjx23cqdj5afn4wqw",
      "start_height": "0",
      "index_offset": "2083033",
      "jailed_until": "1970-01-01T00:00:00Z",
      "tombstoned": false,
      "missed_blocks_counter": "0"
    },
    {
      "address": "zetavalcons134vqf0005w0dlfygqckp7em3sfgvxekdzmlcae",
      "start_height": "0",
      "index_offset": "2083033",
      "jailed_until": "1970-01-01T00:00:00Z",
      "tombstoned": false,
      "missed_blocks_counter": "0"
    },
    {
      "address": "zetavalcons1n06d9v8hz5ffuve8fenyhk7hs8tk0639y56wpk",
      "start_height": "629452",
      "index_offset": "2",
      "jailed_until": "2023-02-03T00:20:09.326230447Z",
      "tombstoned": false,
      "missed_blocks_counter": "2"
    },
    {
      "address": "zetavalcons1mpys3lwp2jv3wq5vwunmt6xhsqmzratn73hkal",
      "start_height": "0",
      "index_offset": "2083033",
      "jailed_until": "1970-01-01T00:00:00Z",
      "tombstoned": false,
      "missed_blocks_counter": "0"
    },
    {
      "address": "zetavalcons1msn5xx766j27ju6u64pvl4hxxuy3jlsyazrfdu",
      "start_height": "1220172",
      "index_offset": "2",
      "jailed_until": "2023-03-14T14:10:09.892193570Z",
      "tombstoned": false,
      "missed_blocks_counter": "2"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "8"
  }
}
```
{% endcode %}
