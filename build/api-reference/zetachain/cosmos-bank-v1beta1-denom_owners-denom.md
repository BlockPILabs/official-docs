---
description: >-
  DenomOwners queries for all account addresses that own a particular token
  denomination.
---

# /cosmos/bank/v1beta1/denom\_owners/{denom}

#### **Parameters:**

**denom-string,** denom defines the coin denomination to query all account holders for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/denom_owners/azeta

// Result
{
  "denom_owners": [
    {
      "address": "zeta1pptfhnyj37qn0nfuhmu7m5ssy5x6td8hlcqa0f",
      "balance": {
        "denom": "azeta",
        "amount": "157215284168870933"
      }
    },
    {
      "address": "zeta1pyks89mqljlpgzenwa0g8zch0hptk6usd9vcuh",
      "balance": {
        "denom": "azeta",
        "amount": "249994658"
      }
    },
    {
      "address": "zeta1p3emgemv8q0fmtw70kfzwecmcvyd9ztqmzy3r9",
      "balance": {
        "denom": "azeta",
        "amount": "99012514498953038523"
      }
    },
    {
      "address": "zeta1zrzrdsxnvshqwf6vvyanejcwe272jkzasjke4d",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000000000000"
      }
    },
    {
      "address": "zeta1zr2wfgnd7fwrwu39gc3chm4yqr3yr4hdwd6ukz",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000000000000"
      }
    },
    {
      "address": "zeta1zm8w95qe2l3yu6k7jxxwwm27wjsczlh9mw9hq6",
      "balance": {
        "denom": "azeta",
        "amount": "20100000000000000000"
      }
    },
    {
      "address": "zeta1r89vknq20lp9txxvg3tya58v5qfynlp328pwkj",
      "balance": {
        "denom": "azeta",
        "amount": "267730226746456650325"
      }
    },
    {
      "address": "zeta1r4khydyslwq39wqaqrwx7kw80s5yrjw5tyshxn",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000800002000"
      }
    },
    {
      "address": "zeta1yq5pqzvasc38mruv9xhs34rfx4lanlm709m7eg",
      "balance": {
        "denom": "azeta",
        "amount": "9999999993799702454"
      }
    },
    {
      "address": "zeta1y438rc9894zluh4muq7w27c80l6sfn67nmhks4",
      "balance": {
        "denom": "azeta",
        "amount": "10000000000000000000"
      }
    },
    {
      "address": "zeta1ymnrwg9e3xr9xkw42ygzjx34dyvwvtc23cnnxz",
      "balance": {
        "denom": "azeta",
        "amount": "9000011119152938905206"
      }
    },
    {
      "address": "zeta1yuwasp3u9m396sfym5j56ftpp2zqv5qxn202ye",
      "balance": {
        "denom": "azeta",
        "amount": "499999968499991034569"
      }
    },
    {
      "address": "zeta19qjs5kpgrmk0mee06k47s7sss95g6s8g34q7gy",
      "balance": {
        "denom": "azeta",
        "amount": "99999999999990304675528"
      }
    },
    {
      "address": "zeta192dfy70up26pushkvt9qfmpr877rx8aspnpvsr",
      "balance": {
        "denom": "azeta",
        "amount": "100981491"
      }
    },
    {
      "address": "zeta19nfaqu9wr0fktyyampva98ec025kjy0phww5um",
      "balance": {
        "denom": "azeta",
        "amount": "4978345522639899988889"
      }
    },
    {
      "address": "zeta19mjzkj5dx0mh2kxhemktkk8zpp8se2sppn2mj9",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000000000000"
      }
    },
    {
      "address": "zeta1xpygth5e97sp46heck6yfrppjm5v0n9wn5wjgy",
      "balance": {
        "denom": "azeta",
        "amount": "99957175"
      }
    },
    {
      "address": "zeta1x0dx6tkjf76jam9d8lrxv2805dpqefnqhhtdf5",
      "balance": {
        "denom": "azeta",
        "amount": "99000000000099857291"
      }
    },
    {
      "address": "zeta1xkddnhcdy5j4auzefjqkt3kp56t6vq7sl57r9t",
      "balance": {
        "denom": "azeta",
        "amount": "99971247"
      }
    },
    {
      "address": "zeta18pksjzclks34qkqyaahf2rakss80mnusju77cm",
      "balance": {
        "denom": "azeta",
        "amount": "9000011117735445947082"
      }
    },
    {
      "address": "zeta18f7wch6kpfdmk6dk9qqhkszpjwrymev4fpte8p",
      "balance": {
        "denom": "azeta",
        "amount": "9000011236732476788103"
      }
    },
    {
      "address": "zeta18wqarvdsvm3sdq86xf4mlnev0wqtvcgg4vnl95",
      "balance": {
        "denom": "azeta",
        "amount": "98969999999999999999795"
      }
    },
    {
      "address": "zeta1ggqzjf5726uu7xc6pfwg00lny79w6t3a3utpw5",
      "balance": {
        "denom": "azeta",
        "amount": "99000000000000000995540"
      }
    },
    {
      "address": "zeta1gsguzysygs633fh7mq8y5yxm7z0pc6k82unt26",
      "balance": {
        "denom": "azeta",
        "amount": "18668424956663567"
      }
    },
    {
      "address": "zeta1g323lusfa9qqvjvupajre2dphuem999fahc086",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999999349652"
      }
    },
    {
      "address": "zeta1g5rqq9jl7zl7sr5wtgtf88ajy72qnmvs6fmwwq",
      "balance": {
        "denom": "azeta",
        "amount": "4999499999654307498973261"
      }
    },
    {
      "address": "zeta1gumvmmf62jxzyth99jasfre6llgeyuu7peksc7",
      "balance": {
        "denom": "azeta",
        "amount": "98999000000000000000"
      }
    },
    {
      "address": "zeta1gl6j2hcv6eeuj9qlmac3q03spn9l6wl5gyfetv",
      "balance": {
        "denom": "azeta",
        "amount": "10000000000000000000"
      }
    },
    {
      "address": "zeta1fxshejs06h9446g9dwavx9knlnsf3tkj4yd4xu",
      "balance": {
        "denom": "azeta",
        "amount": "1000000000799968084"
      }
    },
    {
      "address": "zeta1futgfg5wx06zeh6s4wtw9xnsnctjf8nrcvu9sr",
      "balance": {
        "denom": "azeta",
        "amount": "3000099999999999992561360"
      }
    },
    {
      "address": "zeta1fl48vsnmsdzcv85q5d2q4z5ajdha8yu3rl86r8",
      "balance": {
        "denom": "azeta",
        "amount": "1217830661117627027871569"
      }
    },
    {
      "address": "zeta12p6znulv90fn40f6sa7ap53hdc8jwxw4x5fd70",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999999493563"
      }
    },
    {
      "address": "zeta122cx6fts6cn70lpwg3t40lyh9gm83269tdfn79",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999990698995528"
      }
    },
    {
      "address": "zeta1tygms3xhhs3yv487phx3dw4a95jn7t7lhlmt4n",
      "balance": {
        "denom": "azeta",
        "amount": "104000000000200922265"
      }
    },
    {
      "address": "zeta1tfke4f4mwh398pflz5aknde55z6hdzan5a4xc7",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999999998000"
      }
    },
    {
      "address": "zeta1t5u55hsz48pgmks06fyy3hklt5urdzgxt7tytu",
      "balance": {
        "denom": "azeta",
        "amount": "1000098335865188730350"
      }
    },
    {
      "address": "zeta1tefr77zwmk0wwhvk4fa69tylxygxc5u3gezhff",
      "balance": {
        "denom": "azeta",
        "amount": "500000000099328027"
      }
    },
    {
      "address": "zeta1tu934qn5nj6wyfuweplcha4krrw8r29lxxn924",
      "balance": {
        "denom": "azeta",
        "amount": "772428748443421098574"
      }
    },
    {
      "address": "zeta1v8v7zkyt7j3dc526k4alsu8vspvqqg342t27vu",
      "balance": {
        "denom": "azeta",
        "amount": "249994658"
      }
    },
    {
      "address": "zeta1v2em89xhjv85jxa0sveqatt32czcv2tywmgnzw",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000800001000"
      }
    },
    {
      "address": "zeta1dxyzsket66vt886ap0gnzlnu5pv0y99v086wnz",
      "balance": {
        "denom": "azeta",
        "amount": "9000015759550241409502"
      }
    },
    {
      "address": "zeta1dk3sh7n9apdpdvzmecuyvvu76278gcck2jmfcg",
      "balance": {
        "denom": "azeta",
        "amount": "898970921679918463064"
      }
    },
    {
      "address": "zeta1w8qa37h22h884vxedmprvwtd3z2nwakxu9k935",
      "balance": {
        "denom": "azeta",
        "amount": "9000012997502330569776"
      }
    },
    {
      "address": "zeta1wdd3fwmegces02ktakrd4uej9v0xyf4trw8fja",
      "balance": {
        "denom": "azeta",
        "amount": "99999999990000000"
      }
    },
    {
      "address": "zeta1wwnug5n5e2s2sf0k7t4zcu7enlwj9vq050a6jl",
      "balance": {
        "denom": "azeta",
        "amount": "2100017035340403042543"
      }
    },
    {
      "address": "zeta1w5czgpk5kc9etxw2anzhr0uyrr4fqks32qmk6k",
      "balance": {
        "denom": "azeta",
        "amount": "9000011231453298277535"
      }
    },
    {
      "address": "zeta1w43fn2ze2wyhu5hfmegr6vp52c3dgn0srdgymy",
      "balance": {
        "denom": "azeta",
        "amount": "628"
      }
    },
    {
      "address": "zeta10g9x93lw7hu0cey5fyvewm4lsnuhe8q3zz9cny",
      "balance": {
        "denom": "azeta",
        "amount": "199000000000099977994"
      }
    },
    {
      "address": "zeta10ju8dap0u9wf50akjgapwagcu2kejuu2qfmk0z",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999990365075528"
      }
    },
    {
      "address": "zeta1stkv3amjhaheg4zp57w3es3yx0qf59zdl4vld2",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999990322115528"
      }
    },
    {
      "address": "zeta13sx53p996z6vzwzzetkvhwk5msceml7q6h623u",
      "balance": {
        "denom": "azeta",
        "amount": "43999999999999999736"
      }
    },
    {
      "address": "zeta13cepcmkn5qhzel4mwq3wnewxphvv7g9slp4azc",
      "balance": {
        "denom": "azeta",
        "amount": "1000000167626280973"
      }
    },
    {
      "address": "zeta1369l99rk06qc9pqfpvse3n389jjnp82gy6u5w2",
      "balance": {
        "denom": "azeta",
        "amount": "29855262000000000000"
      }
    },
    {
      "address": "zeta1j8yhw9u7a6kdahg8wpyxy5tzxjjh0f0kwd292z",
      "balance": {
        "denom": "azeta",
        "amount": "4009989999999990741744187"
      }
    },
    {
      "address": "zeta1j8g8ch4uqgl3gtet3nntvczaeppmlxajqwh5u6",
      "balance": {
        "denom": "azeta",
        "amount": "9000011117735447430592"
      }
    },
    {
      "address": "zeta1jv65s3grqf6v6jl3dp4t6c9t9rk99cd83m2fn0",
      "balance": {
        "denom": "azeta",
        "amount": "2951065634396698275"
      }
    },
    {
      "address": "zeta1j003wfefa0v4l7ekl2hlgq7dv7kf95nfj86d5l",
      "balance": {
        "denom": "azeta",
        "amount": "200000000099998000"
      }
    },
    {
      "address": "zeta1ndtnuqa6n3qj7txf2ewuctrjad3jvqz6jdzznd",
      "balance": {
        "denom": "azeta",
        "amount": "89999999999999999960"
      }
    },
    {
      "address": "zeta15ruj2tc76pnj9xtw64utktee7cc7w6vzaes73z",
      "balance": {
        "denom": "azeta",
        "amount": "9000011240329887811396"
      }
    },
    {
      "address": "zeta152ka0ynl4p62wwsesd7rmxpcsdh0z437vf3vyr",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999991397880000"
      }
    },
    {
      "address": "zeta15d004cg8knm8nfklwfpkvfhzcvnl6v0xdkmcmy",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999989727160000"
      }
    },
    {
      "address": "zeta15shzhya7hehe835y6fa0xynrvgvafml6wq7uxm",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000100000000"
      }
    },
    {
      "address": "zeta15un5tst4jmjt6njyyn5dsfchvzrltpc2x3me24",
      "balance": {
        "denom": "azeta",
        "amount": "1000000000098987000"
      }
    },
    {
      "address": "zeta15lshcgxztgmtyg8uv93827ywtswf7jg8yujqvk",
      "balance": {
        "denom": "azeta",
        "amount": "9999903835"
      }
    },
    {
      "address": "zeta14f3dtmvpzegj994778lxa8jryak2z0knmyygpr",
      "balance": {
        "denom": "azeta",
        "amount": "999999999999920000"
      }
    },
    {
      "address": "zeta1kd4r2ahxz0vpzulrqrvr7a9t7ukcchrggvefhn",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999990133315528"
      }
    },
    {
      "address": "zeta1ku7q4tzvresxcmjftkzgr934tektxqup3wvnad",
      "balance": {
        "denom": "azeta",
        "amount": "90375429733079244458"
      }
    },
    {
      "address": "zeta1h3skkjzr78se58vau9sd78gdg9rtek8v8up6q2",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999898978054"
      }
    },
    {
      "address": "zeta1hk05v9len8u0c2xrwxgfknvcskpd4vncm7ehch",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999999879228"
      }
    },
    {
      "address": "zeta1hekzwrn6ccutv4yg5zx5rm8venggy9w4hhag6n",
      "balance": {
        "denom": "azeta",
        "amount": "10000000000099994000"
      }
    },
    {
      "address": "zeta1harefw4y9q7sjkqyg90eywm5v6xrtfurfaa3mw",
      "balance": {
        "denom": "azeta",
        "amount": "4959999873999999412000"
      }
    },
    {
      "address": "zeta1cv5nqpay7p5r2y9apkl97zute45d5je3f06e4j",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999999879308"
      }
    },
    {
      "address": "zeta1ezz0u6t3fcaaw33jlp3lcm3e8zskyafa8tpqj3",
      "balance": {
        "denom": "azeta",
        "amount": "99817916499150277"
      }
    },
    {
      "address": "zeta1e9vzljpcyhg6xh9eefxwfrll2puqzzu5a8xtek",
      "balance": {
        "denom": "azeta",
        "amount": "100000000000800002000"
      }
    },
    {
      "address": "zeta1e8x7gdu6pp49l6pyvu3nfys7a9duumgdj45p6r",
      "balance": {
        "denom": "azeta",
        "amount": "39999999999999653320"
      }
    },
    {
      "address": "zeta1e07th0309p0mh9s03l79yz08ka8ptu6xsza0cc",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999988684309146"
      }
    },
    {
      "address": "zeta1euvlmpffq7gl77vlwlv97kn004zq6rdw0skdd3",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999990552595528"
      }
    },
    {
      "address": "zeta16s3jdj7ykpxqrt8ptdzvatdltc4jdktu9anjza",
      "balance": {
        "denom": "azeta",
        "amount": "89982000"
      }
    },
    {
      "address": "zeta1mr6rqva6d6gnelu7vwl38h0xn7tl67wac7d43e",
      "balance": {
        "denom": "azeta",
        "amount": "4099999999999990367035528"
      }
    },
    {
      "address": "zeta1mte0r3jzkf2rkd7ex4p3xsd3fxqg7q29q0wxl5",
      "balance": {
        "denom": "azeta",
        "amount": "84989999999999999667793"
      }
    },
    {
      "address": "zeta1m30ggxhd2nmjl87xca5wy8g2vytkcxm0zt79ad",
      "balance": {
        "denom": "azeta",
        "amount": "19999801207978329"
      }
    },
    {
      "address": "zeta1mhzh7ecjgcecjrjre2peuef4zfmn94pg8s2htn",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999995343140"
      }
    },
    {
      "address": "zeta1meq97nclpc3vd9zj6y43wvgfncshqg2lplk5gr",
      "balance": {
        "denom": "azeta",
        "amount": "4999999990099959573"
      }
    },
    {
      "address": "zeta1uphzh933k7f2qfp6gajttu5stwlnsk9f0xmj9f",
      "balance": {
        "denom": "azeta",
        "amount": "98999999999999994723316"
      }
    },
    {
      "address": "zeta1utsn7w4dzluh026ylwkntmtc4jrpn2393nsggp",
      "balance": {
        "denom": "azeta",
        "amount": "9999999999987142384"
      }
    },
    {
      "address": "zeta179srm759jvjdpk8m4hcv9m7072zlk6uxtmnuex",
      "balance": {
        "denom": "azeta",
        "amount": "8999968499821741381"
      }
    },
    {
      "address": "zeta17xpfvakm2amg962yls6f84z3kell8c5lxad43d",
      "balance": {
        "denom": "azeta",
        "amount": "200000"
      }
    },
    {
      "address": "zeta17d6ttmqffr5pwt9fd7uuj8px27quv4nlkffv2y",
      "balance": {
        "denom": "azeta",
        "amount": "99921626"
      }
    },
    {
      "address": "zeta17wz3pwd038hzczk2c4js84pzn6ehhctf8wurja",
      "balance": {
        "denom": "azeta",
        "amount": "9994025534483652305"
      }
    },
    {
      "address": "zeta1l2dwhqy94687yja0upaq0v5aukgdepfw0y253j",
      "balance": {
        "denom": "azeta",
        "amount": "99799999999990157271056"
      }
    },
    {
      "address": "zeta1lhpdmdklsnkkx8sj4a8devhjqtsgt478hjq7au",
      "balance": {
        "denom": "azeta",
        "amount": "100000000"
      }
    },
    {
      "address": "zeta1luc7fqtw8k2kex8q0y65mzahk0rcvvcc0fyyau",
      "balance": {
        "denom": "azeta",
        "amount": "899856823481954329"
      }
    },
    {
      "address": "zeta1dlszg2sst9r69my4f84l3mj66zxcf3umcgujys30t84srg95dgvs5wguxq",
      "balance": {
        "denom": "azeta",
        "amount": "100000"
      }
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "93"
  }
}
```
{% endcode %}
