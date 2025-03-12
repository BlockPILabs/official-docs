---
description: >-
  Get basic information about the address: balance, code, data,
  last_transaction_id.
---

# /getAddressInformation

**Parameters**

**address - string,** Identifier of target TON account in any form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getAddressInformation?address=UQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVxtU' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "raw.fullAccountState",
    "balance": "14020735",
    "code": "te6cckECFAEAAtQAART/APSkE/S88sgLAQIBIAIDAgFIBAUE+PKDCNcYINMf0x/THwL4I7vyZO1E0NMf0x/T//QE0VFDuvKhUVG68qIF+QFUEGT5EPKj+AAkpMjLH1JAyx9SMMv/UhD0AMntVPgPAdMHIcAAn2xRkyDXSpbTB9QC+wDoMOAhwAHjACHAAuMAAcADkTDjDQOkyMsfEssfy/8QERITAubQAdDTAyFxsJJfBOAi10nBIJJfBOAC0x8hghBwbHVnvSKCEGRzdHK9sJJfBeAD+kAwIPpEAcjKB8v/ydDtRNCBAUDXIfQEMFyBAQj0Cm+hMbOSXwfgBdM/yCWCEHBsdWe6kjgw4w0DghBkc3RyupJfBuMNBgcCASAICQB4AfoA9AQw+CdvIjBQCqEhvvLgUIIQcGx1Z4MesXCAGFAEywUmzxZY+gIZ9ADLaRfLH1Jgyz8gyYBA+wAGAIpQBIEBCPRZMO1E0IEBQNcgyAHPFvQAye1UAXKwjiOCEGRzdHKDHrFwgBhQBcsFUAPPFiP6AhPLassfyz/JgED7AJJfA+ICASAKCwBZvSQrb2omhAgKBrkPoCGEcNQICEekk30pkQzmkD6f+YN4EoAbeBAUiYcVnzGEAgFYDA0AEbjJftRNDXCx+AA9sp37UTQgQFA1yH0BDACyMoHy//J0AGBAQj0Cm+hMYAIBIA4PABmtznaiaEAga5Drhf/AABmvHfaiaEAQa5DrhY/AAG7SB/oA1NQi+QAFyMoHFcv/ydB3dIAYyMsFywIizxZQBfoCFMtrEszMyXP7AMhAFIEBCPRR8qcCAHCBAQjXGPoA0z/IVCBHgQEI9FHyp4IQbm90ZXB0gBjIywXLAlAGzxZQBPoCFMtqEssfyz/Jc/sAAgBsgQEI1xj6ANM/MFIkgQEI9Fnyp4IQZHN0cnB0gBjIywXLAlAFzxZQA/oCE8tqyx8Syz/Jc/sAAAr0AMntVGliJeU=",
    "data": "te6cckEBAQEAKwAAUQAAAAIpqaMXC4yW0mQyIVSJAFroGZSCTwJNiZWBrrQ0WTHPLeJONxtAH8te9g==",
    "last_transaction_id": {
      "@type": "internal.transactionId",
      "lt": "48756545000001",
      "hash": "JseckUUQ5BOUW3fAmggsXknXxQGwtoVwuo1/qTuDRDo="
    },
    "block_id": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984035,
      "root_hash": "4ufbBY6tzDif9bWxIlsn+ZCQfS/dXOsdRb6/pPrIb9I=",
      "file_hash": "riAbHvuG/JV/ZWc5u2Ukx7g7ZdyeY5vLQ+kYGyB5bnM="
    },
    "frozen_hash": "",
    "sync_utime": 1724742404,
    "@extra": "1724742614.8329434:5:0.5900705580417361",
    "state": "active"
  }
}
```
{% endcode %}
