---
description: >-
  Returns a list with a textual summary of all the transactions currently
  pending for inclusion in the next block(s), as well as the ones that are being
  scheduled for future execution only.
---

# txpool\_inspect

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_inspect","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": {
            "0x0003b351Cb791af29e970553f7CF035A33CA1FBF": {
                "58473": "0xFC334e057bd936e8ceda6A8B1C7b655E9Ad70946: 280000000000000 wei + 21000 gas × 5000000000 wei"
            },
            "0x00a2013A984FfCC9d1412d5ad76A9d7FfD6Ee1A9": {
                "22": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0x10923edCc66D518EC7BD4a50F39a8Eb6f2b346AF": {
                "3514": "0xce93F9827813761665CE348e33768Cb1875a9704: 0 wei + 81999 gas × 1000000000 wei"
            },
            "0x1542d33bEF57cD4Af632330E817b62701958B39D": {
                "17": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0x16A28fcC74514DeE4Ae44152108CaCedB732C3bE": {
                "16": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0x18ed78f425728b9748EcA2C7070d4F8D5bD34e61": {
                "2": "0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2: 0 wei + 298589 gas × 5000000000 wei"
            },
            "0x1C9f9e136F5c321222c840Fa744F32ff2Ba8CCB2": {
                "15": "0x55d398326f99059fF775485246999027B3197955: 0 wei + 51115 gas × 5010000000 wei"
            },
            "0x1a478bEF41BfeacDceCbee96b5450aa842379D2F": {
                "218": "0x3724a6Fd23FeF6a97a90aa61f76e8caF65865971: 5000000000000000 wei + 21000 gas × 5000000000 wei"
            },
            "0x2066f6024Ff59271F35040E40660345515950261": {
                "505": "0xb45A2DDA996C32E93B8c47098E90Ed0E7ab18E39: 0 wei + 499576 gas × 5010000000 wei"
            },
            "0x2634EBe9d791FD39A24D157D90bE2A19BC6de625": {
                "25": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0x29D8C54FafB5392E26d89Dc2Ab2BA52Fe2b6bf9b": {
                "143046": "0x31B8A8Ee92961524fD7839DC438fd631D34b49C6: 0 wei + 300000 gas × 5100000000 wei"
            },
            "0x2d8d9c8305426F5f8b28efaC15a9eCC9C1D043aE": {
                "3": "0x4b136E073D469f240983ACe06e3c5f776FCE45Ea: 0 wei + 70000 gas × 5000000000 wei"
            },
            "0x2fb6509633523F2B795EA01f5337e3b9e1e53d4E": {
                "226": "0xDE8d0B3d77e9A2507a56c392b6f450a2db5d25E6: 0 wei + 109631 gas × 5010000000 wei"
            },
            "0x3023b2c1A6C2d395A56ECC3903E2f9F15962ac3e": {
                "28": "0xf84f56f54c0C0F6E981EEC0e4C14025D2B3b4C94: 0 wei + 388966 gas × 5000000000 wei"
            },
            "0x32fF73949B0252c284564aaec64C91e8e5178D6e": {
                "38165": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56: 0 wei + 500000 gas × 5000000000 wei"
            },
            "0x3467AF77a998cEFcE674582C385B6Af7C94eF787": {
                "779": "0x4de2b5D4a343dDFBeEf976B3ED34737440385071: 0 wei + 193733 gas × 2000000000 wei"
            },
            "0x39f84554E5a26B1D059274278745712b8B7494eD": {
                "21": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0x4Cb37A81899883b7369309a4ad305D5c5c62eF52": {
                "63": "0xD8f1dDD20DF17E8BcCD481Db1482A6963ae62d4f: 0 wei + 55019 gas × 5010000000 wei"
            },
            "0x521c7ACC90FA6CDFfA34feBdFA549Ce1aE7F116A": {
                "20": "0xbc82e8c98d2adAFA825668f685F3C3e51DdC4F8B: 0 wei + 702870 gas × 5000000000 wei"
            },
            "0x527FBBfB5789a26F7B41926D352190273B155677": {
                "12": "0x55d398326f99059fF775485246999027B3197955: 0 wei + 51127 gas × 5010000000 wei"
            },
            "0x5764F360CB68FD3E0C0B06e92AB99Cce2aDF14B4": {
                "3": "0x4b136E073D469f240983ACe06e3c5f776FCE45Ea: 0 wei + 70000 gas × 5000000000 wei"
            },
            "0x60328e896Ad639D2EC642c3fCf9aDEC824B41119": {
                "2": "0xb9a5BDe0a19288044784B859c903Ee62fF2a3A65: 0 wei + 27112 gas × 5000000000 wei"
            },
            "0x6b039289BA4F18ff621635855905464E8303A649": {
                "590": "0xAe5F14A9aed2b56121fb964A84a9DFf114296563: 0 wei + 850000 gas × 7000000000 wei"
            },
            "0x6d5C83cb36aa3EaFC1A41E197b9f1Ce415B8cd09": {
                "6": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0x6e661D9A6c8E4145CE86a243d2E3254aaA31AbA8": {
                "1": "0x76C49a0d31729b7BE3970a28c7B6DDEc2717ecA5: 0 wei + 345067 gas × 5000000000 wei"
            },
            "0x7728300dfe6d53C884C712438B3db78ee5BAc73E": {
                "15": "0x3B5bbE51e85c83a5E11fE62363C25aC5BB970451: 608350000000000 wei + 21000 gas × 5000000000 wei"
            },
            "0x81f25E82e66c519adEf3D193426214f805eA40b7": {
                "715": "0x9A36AdfaF32A9494d6618340C42b8Ac813fD1d37: 0 wei + 480000 gas × 1010100000 wei"
            },
            "0x8d89D24D7D1Bce68d04D7D2c7E93DF94d7d7b564": {
                "65": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c: 0 wei + 65910 gas × 5000000000 wei"
            },
            "0x9065b28af06B06e3879d43920EF5224bD0E5361f": {
                "0": "0xb9a5BDe0a19288044784B859c903Ee62fF2a3A65: 0 wei + 42113 gas × 5000000000 wei"
            },
            "0xA0c48d24465B8FB21224F4D42Ad93D84D0483b38": {
                "1553": "0x897765bE1384A568FbCdbE280C6402D61E85e96d: 0 wei + 186359 gas × 1000000000 wei"
            },
            "0xAED302EB3BDc04A21cA4d171764C94d08a0f728a": {
                "380": "0x10ED43C718714eb63d5aA57B78B54704E256024E: 171700000000000000 wei + 310000 gas × 5000000000 wei"
            },
            "0xAEa3D1d8EeAc0D71132a59cA1c72D814bc61D2d1": {
                "19": "0x3495d311cB062199309eD17E6cA82A8F9fde8B5A: 0 wei + 25000 gas × 5000000000 wei"
            },
            "0xBC76F61a65e49c24482a3b87088ac428C934eA93": {
                "580": "0x53eef4D1C08A240d4C42b1C4522F37999972d180: 3000000000000000 wei + 21000 gas × 5010000000 wei"
            },
            "0xBa43d6e1Ce93E32b60f656509cA90839968E6D19": {
                "77": "0x55d398326f99059fF775485246999027B3197955: 0 wei + 54154 gas × 5000000000 wei"
            },
            "0xBc9A201cf79cCDED23f888cc8375c6Ab6e0Fa9ef": {
                "402": "0x2723522702093601e6360CAe665518C4f63e9dA6: 0 wei + 143942 gas × 1200000000 wei"
            },
            "0xE40392e5C0cDB7d15727Bce5F31cA3f54a241e9B": {
                "2": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            },
            "0xE64B65F994Bd085229E17b30aEe5393d29210FEa": {
                "141730": "0xF2f99Ac877b01B12CD9Cb98c9546067eD255ef0e: 580000000000000 wei + 116000 gas × 5000000000 wei"
            },
            "0xc729C1DF98A2fE931ECDf07E1D6c4498F605441D": {
                "184": "0x19D91bBc5943D9eCeC96B159A608d0bAe12B1640: 0 wei + 71478 gas × 10000000000 wei"
            },
            "0xe2fc31F816A9b94326492132018C3aEcC4a93aE1": {
                "12985797": "0xF8A0BF9cF54Bb92F17374d9e9A321E6a111a51bD: 0 wei + 207128 gas × 10000000000 wei",
                "12985798": "0x715D400F88C167884bbCc41C5FeA407ed4D2f8A0: 0 wei + 207128 gas × 10000000000 wei"
            },
            "0xe9953CC11f9058D5a8fac0e4AFE64126a884dAA9": {
                "472": "0x1066E779E06bB380b494A9b3ac0ce6102402BCc4: 13000000000000000 wei + 21000 gas × 5000000000 wei"
            },
            "0xf79f1B37Ef70C6c10cCDF43Fc83791288F16F76B": {
                "11": "0x3d24C45565834377b59fCeAA6864D6C25144aD6c: 0 wei + 28534 gas × 5000000000 wei"
            }
        },
        "queued": {
            "0x3B8b73685ffE40fB42Aa62C38FCb0A49454c6EAb": {
                "211": "0x4de2b5D4a343dDFBeEf976B3ED34737440385071: 0 wei + 160907 gas × 1000000000 wei",
                "212": "0x4de2b5D4a343dDFBeEf976B3ED34737440385071: 0 wei + 160907 gas × 2000000000 wei",
                "213": "0x4de2b5D4a343dDFBeEf976B3ED34737440385071: 0 wei + 160907 gas × 5000000000 wei",
                "214": "0x4de2b5D4a343dDFBeEf976B3ED34737440385071: 0 wei + 160907 gas × 5000000000 wei",
                "215": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 1000000000 wei",
                "216": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 1000000000 wei",
                "217": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 5000000000 wei",
                "218": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 5000000000 wei",
                "219": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 1000000000 wei",
                "220": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 5000000000 wei",
                "221": "0x1745A5Be4497b4eC1E9666516BD81d8608471D4b: 0 wei + 109008 gas × 5000000000 wei",
                "222": "0xce93F9827813761665CE348e33768Cb1875a9704: 1825000000000000 wei + 153817 gas × 1000000000 wei",
                "223": "0xce93F9827813761665CE348e33768Cb1875a9704: 0 wei + 86092 gas × 1000000000 wei"
            },
            "0x999999E80aaFb9bcA63361815A53f897C4bB7661": {
                "57692": "0x000000000080bFb4319A2d940140bf073CaC846b: 0 wei + 80000 gas × 5500000000 wei"
            },
            "0xBF702AB9E3eC058f56b4E03adEdfBfdC72f413cA": {
                "577": "0xED483116Cc309347997FE139e2256F1cbEa140D6: 50000000000000 wei + 21000 gas × 5000000000 wei"
            }
        }
    }
}
```
{% endcode %}
