---
description: TotalSupply queries the total supply of all coins.
---

# /cosmos/bank/v1beta1/supply

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/supply

// Result
{
    "supply": [
        {
            "denom": "ibc/00255B18FBBC1E36845AAFDCB4CBD460DC45331496A64C2A29CEAFDD3B997B5F",
            "amount": "1016160059457055549180"
        },
        {
            "denom": "ibc/0030B0AA8A1B9028703B1D17B965FBCBE0136571B854410BFEC3475B1DC765A1",
            "amount": "43210"
        },
        {
            "denom": "ibc/0276EC3A17E2BADE81821D73FE20CB6D71487F151FEE36E159962B8721942F9D",
            "amount": "1000000"
        },
        {
            "denom": "ibc/03D28CFE7A878F122AB9727064E916B12FB88AFEC7CFF0DCBD1F9028399EB06F",
            "amount": "955679751"
        },
        {
            "denom": "ibc/03FDDDFA51B58B17520629DD2082A9D8B2D72FA06BD060E660006ACF9D9AF58C",
            "amount": "100000000000000000"
        },
        {
            "denom": "ibc/048ACDA78D3A363F7FC099F52E4B5993DB8533891E0ECA032EDB6BEF2BCDCA25",
            "amount": "130000"
        },
        {
            "denom": "ibc/04AA0759B8FF54DFEE563C6046050953D77079A7D212AF59E4C80FCBF98247CA",
            "amount": "2500000"
        },
        {
            "denom": "ibc/04F26F89E89475EBEDA75428CD312CF2DF569A3ED0C999CAC1CCA151FF30694A",
            "amount": "5000000000"
        },
        {
            "denom": "ibc/07912C24004932CD561B1751562B22EA787F31F9821568B88F55A8F51D326722",
            "amount": "5000"
        },
        {
            "denom": "ibc/07D6E70DC599BBD2A768CDBA64DF4CAD1DC852EA3DE5453A64C66CBA9689350C",
            "amount": "1999999999997000000"
        },
        {
            "denom": "ibc/07E2BE32D224C2F0EA3267E0A4673C37B952F9C3C2CFE7916FBA9079492BB4D6",
            "amount": "1000000000"
        },
        {
            "denom": "ibc/080D7604D9C1960A3562E1AE4E8EA8F30B7813810AE30660D41DD6770B1C5929",
            "amount": "2000000000"
        },
        {
            "denom": "ibc/08822F65D0CE3FD27B35B9E99046CBAB72D731C7991BBC8586E8916F78721FEF",
            "amount": "100000"
        },
        {
            "denom": "ibc/08834A76F4E5AED08690916F61EA12AA71CFD636BBA328062027DF9FA620B7E3",
            "amount": "1"
        },
        {
            "denom": "ibc/091F39508BB813883D43F29461C7EBC2DD480319B659FAB583129D78A9A2D22E",
            "amount": "431157000000000001"
        },
        {
            "denom": "ibc/09334FF8B9AD27E39D37E3B80E73F48474289173AEFBB285BAD4D4B256707C46",
            "amount": "12016457"
        },
        {
            "denom": "ibc/0A327721C1317DD492ABC7A8B5DE70A3131CECD111881EA740A1E72BE20EA41A",
            "amount": "100000"
        },
        {
            "denom": "ibc/0B38A5C88FD41B958A853224D34ECF5B1C6630ACF85AAA3655622BFF5D934C39",
            "amount": "792195"
        },
        {
            "denom": "ibc/0C754B423F325B3C8DEBD837CE7C4CF0D4B0E60BEB710E8C8C2E231769DC357C",
            "amount": "103000"
        },
        {
            "denom": "ibc/0D33E2077E140784912451ED189B11D78A4CD10C480C39E0CD91C67B1406B69F",
            "amount": "21369574639"
        },
        {
            "denom": "ibc/0E018ACFCF79C355EBC45DDDB27B03ADB989D1DC976840BAACF81619EE47FDEF",
            "amount": "1000000"
        },
        {
            "denom": "ibc/0E394468DF71E51FA3702264562CCECBF1E198C12D13178189385B4C432E0264",
            "amount": "200000000000000"
        },
        {
            "denom": "ibc/0EFC9CE517D5C868C23FB91F31B22AA1FA4B63BD7CC583BD5855F45F5DBF99BB",
            "amount": "1"
        },
        {
            "denom": "ibc/0F123D0CF1614D8C6021E9342FF3C84D55B6BC306B2EF05CA07D89F6005BD6B2",
            "amount": "1002000"
        },
        {
            "denom": "ibc/104BF1D9079A5833F018CC3840779D668021400F052F93F88000019F9939150B",
            "amount": "113608"
        },
        {
            "denom": "ibc/1063D42B186F4305F1A9F65D2C9C817D55357D5B5102E177E6A404AE4CC6D561",
            "amount": "100000"
        },
        {
            "denom": "ibc/12DA42304EE1CE96071F712AA4D58186AD11C3165C0DCDA71E017A54F3935E66",
            "amount": "622568105186"
        },
        {
            "denom": "ibc/13B770F3AA627CCD99D3275DEF01D74199472BDCAEE01E4C2646059143B47309",
            "amount": "46657780"
        },
        {
            "denom": "ibc/13EB10FAE4E4E30658875B17E1338924D3EDEB8567011C3F61327E6FCBB3EAA6",
            "amount": "9000"
        },
        {
            "denom": "ibc/1452F322F7B459CB7EC111AD5BD2404552B011375002C8C85BA615A95B9121CF",
            "amount": "26388000591484336715"
        },
        {
            "denom": "ibc/146119BC46E69DEC6BA554A368FF97E7E2D32BA96B57A5D5B169667C91D8528E",
            "amount": "1885000"
        },
        {
            "denom": "ibc/14F9BC3E44B8A9C1BE1FB08980FAB87034C9905EF17CF2F5008FC085218811CC",
            "amount": "146679091609"
        },
        {
            "denom": "ibc/1514A972E1FDA7311B0BFC9756B8D63AE0945279005D8DCC5751E3476AABB8F6",
            "amount": "9500"
        },
        {
            "denom": "ibc/1542F8DC70E7999691E991E1EDEB1B47E65E3A217B1649D347098EE48ACB580F",
            "amount": "1376135230"
        },
        {
            "denom": "ibc/164D296F37491098DBBEB9AD5E53769B07B2A2CEEA43977CA673AA75A75C740A",
            "amount": "17000000000000000000"
        },
        {
            "denom": "ibc/169D83A4FBC7F348FD03BBA25D153802EE1B1056F2718190AD6E00D68BA2EB8E",
            "amount": "500"
        },
        {
            "denom": "ibc/16B4F27D93497DF5F9134457EDF18796F0727CCEB9FA048727D1846F4C6CD4E9",
            "amount": "10098"
        },
        {
            "denom": "ibc/17044DE725FD1979ADA26CA1DF34BDF53D663252B3B50EFE865EC2BE7F152BD8",
            "amount": "90996"
        },
        {
            "denom": "ibc/178F0665CC78FD6ACA40E3ED23A728D96592B29961D3B29CD8F6088CB28D498F",
            "amount": "1000"
        },
        {
            "denom": "ibc/1817C5D173194CEB954020E582DDA166DECD9A511618465940D8D739D7736E22",
            "amount": "50000000000000"
        },
        {
            "denom": "ibc/187ED12F225EB7178ED4ED4DAA09BA5912569B0C71AD48F2F9F58A9CB1B17436",
            "amount": "13819744615384615386"
        },
        {
            "denom": "ibc/188844D75719178A653C3783421F9731759815FE2D58BD37F612D954308A526E",
            "amount": "1130000293761"
        },
        {
            "denom": "ibc/18B534F7278D446966334AD1216A20E6DAB23BB572F24B0A5353BA9760F1BDDF",
            "amount": "14"
        },
        {
            "denom": "ibc/19DD710119533524061885A6F190B18AF28D9537E2BAE37F32A62C1A25979287",
            "amount": "1517201321061996673251"
        },
        {
            "denom": "ibc/19E0FA42DAD7753295D1BDE44B77F7B678CAD8083EFAE043F7D51DF6501EED63",
            "amount": "1927000"
        },
        {
            "denom": "ibc/1A4215832B566E4C2CAE897E4A60EBB9498A5B879DDDA5EC3C21450632D6CD68",
            "amount": "500"
        },
        {
            "denom": "ibc/1AA15279AD043C26508AF9FA8AD4A318A5688071397A350EA86807EDA7327720",
            "amount": "34239255157100000000012"
        },
        {
            "denom": "ibc/1B72F641120380AB0B789F6A46B7F33B192A09FF93CBCC299044E7953FF5AC09",
            "amount": "2000"
        },
        {
            "denom": "ibc/1BABB967BF30E33148F16C763D7E534CD6ED7A908930E6FB5BEFC4DE811286C2",
            "amount": "987654"
        },
        {
            "denom": "ibc/1BD6C2F8186E5E7842F5BA40530AAC71B209D49FC54ACB408126D2372448A202",
            "amount": "1"
        },
        {
            "denom": "ibc/1BE91D67775723D3230A9A5AC54BB29B92A5A51B4B8F20BBA37DF1CFA602297C",
            "amount": "2124798358393"
        },
        {
            "denom": "ibc/1BF8329D782C76B7C600A4AE9D61655D6AC3F957BCB0C73D21F2ACCC60419FBE",
            "amount": "600000"
        },
        {
            "denom": "ibc/1C73D5251879C4BB83106E890EE33BF5464D22066FCDCA5ECCA7CC5705AE13D5",
            "amount": "1000000"
        },
        {
            "denom": "ibc/1C96AAF51605ACF5E4A9672B906E952E936A3E98B39FCD9EFE6ECE93A47DCEF6",
            "amount": "1777"
        },
        {
            "denom": "ibc/1D40A21B46D4C9FF9DC1F34FEC2DA3C9C9FFA8D9494CAE3089C1E08839F058F9",
            "amount": "500000"
        },
        {
            "denom": "ibc/1D5826F7EDE6E3B13009FEF994DC9CAAF15CC24CA7A9FF436FFB2E56FD72F54F",
            "amount": "255038609782775"
        },
        {
            "denom": "ibc/1E87B2416DD2B09BFE1BAA2A8A9F70C5F2B00317BAA2310DC08CCF0B7D29DBED",
            "amount": "20000000"
        },
        {
            "denom": "ibc/1EBF01C38EDC455EA6C40EDC407619EB967ADDA7C3AAB772B66D354A22AFBF4F",
            "amount": "10200"
        },
        {
            "denom": "ibc/1FBDD58D438B4D04D26CBFB2E722C18984A0F1A52468C4F42F37D102F3D3F399",
            "amount": "69321887657"
        },
        {
            "denom": "ibc/20A7DC8E24709E6F1EE0F4E832C2ED345ADD77425890482A349AE3C43CAC6B2C",
            "amount": "36415001"
        },
        {
            "denom": "ibc/2104449BE63E3393371B1BAEEA0D5AF52D2C4E2CCD1C60493FD26FBF56959C21",
            "amount": "200000000000000000"
        },
        {
            "denom": "ibc/21365569E56F540D26CA846D0947C9DE6E482F9291B0D1F884D5681B745C7462",
            "amount": "100"
        },
        {
            "denom": "ibc/2154552F1CE0EF16FAC73B41A837A7D91DD9D2B6E193B53BE5C15AB78E1CFF40",
            "amount": "1284259"
        },
        {
            "denom": "ibc/2181AAB0218EAC24BC9F86BD1364FBBFA3E6E3FCC25E88E3E68C15DC6E752D86",
            "amount": "403813455127"
        },
        {
            "denom": "ibc/220BD71C8801461B5AF45C3B1BFFE5B128613C6919C52FBDFA284BB6BF3F9A7F",
            "amount": "1000000"
        },
        {
            "denom": "ibc/239D0A5417EB70F4B519A82992900FDD8D51885905C893C9194540DD79261EAE",
            "amount": "7660131"
        },
        {
            "denom": "ibc/239E94AA57B7BF7050C8C38611654ECBA10042A6BCA0B6FFE3E7F59FEE2156E0",
            "amount": "46000000000000000"
        },
        {
            "denom": "ibc/23DCE674BC0760CE99F26CBF281ED46F9653ACE3BD490CBBE6103A4D73221637",
            "amount": "2"
        },
        {
            "denom": "ibc/251C380902B42B822975429A22A75AA1F2D0F2DD9E2EFC4BB0F6D00E8C8F6E55",
            "amount": "4000"
        },
        {
            "denom": "ibc/261375CF6694595D0627A3FA10E9A6B580078EB7FB30E55618CDF5D87C4E5AFB",
            "amount": "34787754"
        },
        {
            "denom": "ibc/26D5710650B26F38CD59EDDC2E85830BC47BD727F23747EB41F350263F08DCF7",
            "amount": "5000"
        },
        {
            "denom": "ibc/2860A66FFC565B72381D40777FBABC15F121160DBDDFF13FA62852A52FF76BB7",
            "amount": "65431"
        },
        {
            "denom": "ibc/29A28F2275A029E70751B8A2FDFD165DA5E6BE8AE66EA16973F6B6BD3B75984D",
            "amount": "528722"
        },
        {
            "denom": "ibc/29B5CB3A3CF45C9DD637D85810F69A4C439E359E1C672A1672E04BEA351C1249",
            "amount": "470000"
        },
        {
            "denom": "ibc/2A23796174090DCC8F258E1B0F830319AEFBCD8AA87C1DCB8BDB150AAD300624",
            "amount": "18548089431497600"
        },
        {
            "denom": "ibc/2A46588202CCCC3320031F8E9C5DB26F47E1E9B39924E6FC5C3CE92BC9543891",
            "amount": "100000"
        },
        {
            "denom": "ibc/2C3E071FC6D2C3C60C55773DCBCDD0C297A75439FF945FE646D49944DAD23862",
            "amount": "1110908"
        },
        {
            "denom": "ibc/2C5A03312F1FD426F0CF174A12D3D0ADBDA55C3A5BA15C7D15020A038E02C434",
            "amount": "120000"
        },
        {
            "denom": "ibc/2DA259C27548A9DAD3B60BB57AF71BFEB32646EBB71237ADE7088264B809969C",
            "amount": "34550000000000"
        },
        {
            "denom": "ibc/2EBF11670AE7F1C6CFC7390E477EA2783441F8CEFDAE03D36D4D94BE3A67B337",
            "amount": "100000000"
        },
        {
            "denom": "ibc/2FE3BC121A18E75797637A73EAB543736462549E6E427C368DEBE90C3570312C",
            "amount": "90674487"
        },
        {
            "denom": "ibc/30942D3854C79711654545073D2D6C7A59CA6C87FFD3792CF45EE6E3532B58E9",
            "amount": "1000"
        },
        {
            "denom": "ibc/311A6F75115762F88F2AC7D7110C2694547CACA43110A8B523DEBBE7E6591E1A",
            "amount": "500000"
        },
        {
            "denom": "ibc/3156D8BAD27478B0304EA36CF1D714E4A9BC2196E8038EDB40AC3E37689E7E3F",
            "amount": "444413439"
        },
        {
            "denom": "ibc/3244F601E0E808A9656E5639AD877F6E3070C7EFEFFE9D9A0179EC416CFA955E",
            "amount": "5"
        },
        {
            "denom": "ibc/3353ECFE33281DE5F84FEDDDFF495E5EBD53E9E4385F8ACCC81D456C93735EC7",
            "amount": "126626870202052992967"
        },
        {
            "denom": "ibc/33A9D0DEFC6ECAE9A8931D42660C2E74180BEF7C7DEF217E4AAD6D81C18EB06F",
            "amount": "99533000"
        },
        {
            "denom": "ibc/34CEF8B6A6424C45FE3CCC4A02C9DF9BB38BACC323E08DFFEFE9E4B18BB89AC4",
            "amount": "861150024"
        },
        {
            "denom": "ibc/3628112107EDE324E09660F1DB37A47FCDD64B6C81C19BF4C58AE7B69305F06E",
            "amount": "68544003871743652"
        },
        {
            "denom": "ibc/364D5AB672D6E8FCCCF59417CC2F8E66CC7CCA937B68D9D9FF800E141B51523A",
            "amount": "4620936"
        },
        {
            "denom": "ibc/368B2285E53071AD6FA3856E0D19BAA7350CD2654F1BDD780765505FDDDE5DE9",
            "amount": "10"
        },
        {
            "denom": "ibc/36ADA5E5F0BBC173A043098E1752AC0E5ACD7478A9367E63BB7213BA87C95E17",
            "amount": "1522389"
        },
        {
            "denom": "ibc/370155D4E21CF406A8942C75970D2C27E51F101C95C60A7AD772A72EE03D7A1C",
            "amount": "80000"
        },
        {
            "denom": "ibc/3792246C7C422C037C603C955F8383B4E32E7555D693344F9A029A67FE221C57",
            "amount": "20162400000000000000"
        },
        {
            "denom": "ibc/37D8CDB76A194CF09364637F00CDC9FBF995041715C191D17D7B9DE5F2504AE1",
            "amount": "5264780191"
        },
        {
            "denom": "ibc/393D4E7397A1C3CAB7D8584AE8414E0B9CABE1E60C4F0ED11FC84EE9836816CF",
            "amount": "310248"
        },
        {
            "denom": "ibc/3A1278171A373AF397E56171B443E29D057F5B30955DBA5C5EA920ADC67E99BB",
            "amount": "1"
        },
        {
            "denom": "ibc/3A5D749707E5F0A5231929E5ED76A1EDC4E0F73E8837385455A30B8BBF5B6CF1",
            "amount": "85500000"
        },
        {
            "denom": "ibc/3A7052A4CC7F3056075E770E4406F52F557CDB13849752445F9E69EF7664DBBC",
            "amount": "30100"
        },
        {
            "denom": "ibc/3AE129A4129A68BD569B985E887757B4FD0F9E24B86E04ED3917060D32BAF569",
            "amount": "1"
        }
    ],
    "pagination": {
        "next_key": "aWJjLzNCMzYyREREOTk4NzlENUJBMTk5QTI2NUM1QkJENDZBRTEzOUNBOUY0NkI1Q0ZDREU5QzU5RDY4NzkyODI1QzQ=",
        "total": "490"
    }
}
```
{% endcode %}
