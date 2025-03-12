---
icon: wallet
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Manually Add Network in MetaMask

Sometimes the MetaMask won't let you change the network settings like the Ethereum Mainnet. In this case you can add a new Ethereum Mainnet.

{% stepper %}
{% step %}
Follow the same steps to the Settings

<figure><img src="../../.gitbook/assets/MetaMask Tutorial 3.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Go to the tab of Network.

<figure><img src="../../.gitbook/assets/MetaMask Tutorial 4.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Click Add network.&#x20;

<figure><img src="../../.gitbook/assets/MetaMask Tutorial 8.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Input the network info:

* Network Name: BlockPI Ethereum Mainnet
* Chain ID: 1
* New RPC URL: https://ethereum.blockpi.network/v1/rpc/\<your key>
* Currency symbol: ETH
* Block Explorer: [https://etherscan.io](https://etherscan.io/)

<figure><img src="../../.gitbook/assets/manually add network in metamask 3.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Metamask will automatically switch to this network afterward.&#x20;

BlockPI Ethereum Mainnet will be on the network list. When you switch to this network you are using the BlockPI RPC service.&#x20;
{% endstep %}
{% endstepper %}

### Network infos:

{% tabs %}
{% tab title="Ethereum" %}
<table><thead><tr><th width="579">Specs</th><th width="97">Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Ethereum Mainnet</p><p><strong>Chain ID</strong>: 1</p><p><strong>New RPC URL</strong>: https://ethereum.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://etherscan.io/">https://etherscan.io/</a></p></td><td><p></p><p></p><p>Mainnet</p></td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Ethereum Sepolia</p><p><strong>Chain ID</strong>: 11155111</p><p><strong>New RPC URL</strong>: https://ethereum-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: SepoliaETH</p><p><strong>Block Explore</strong>r: <a href="https://sepolia.etherscan.io/">https://sepolia.etherscan.io/</a></p></td><td><p></p><p></p><p>Sepolia</p></td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Ethereum Holesky</p><p><strong>Chain ID</strong>: 17000</p><p><strong>New RPC URL</strong>: https://ethereum-holesky.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explore</strong>r: <a href="https://holesky.beaconcha.in">https://holesky.beaconcha.in</a></p></td><td>Holesky</td></tr></tbody></table>
{% endtab %}

{% tab title="Kaia" %}
<table><thead><tr><th width="559">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Kaia Mainnet</p><p><strong>Chain ID</strong>: 8217</p><p><strong>New RPC URL</strong>: https://kaia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: KAIA</p><p><strong>Block Explorer</strong>: <a href="https://kaiascope.com">https://kaiascope.com</a></p></td><td><p></p><p></p><p>Mainnet</p></td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Kaia Testnet-Kairos</p><p><strong>Chain ID</strong>: 1001</p><p><strong>New RPC URL</strong>: https://kaia-kairos.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: KAIA</p><p><strong>Block Explorer</strong>: <a href="https://kairos.kaiascope.com/">https://kairos.kaiascope.com/</a></p></td><td><p></p><p></p><p>Kairos</p></td></tr></tbody></table>
{% endtab %}

{% tab title="Polygon" %}
<table><thead><tr><th width="577">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Polygon Mainnet</p><p><strong>Chain ID</strong>: 137</p><p><strong>New RPC URL</strong>: https://polygon.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: MATIC</p><p><strong>Block Explorer</strong>: <a href="https://polygonscan.com/">https://polygonscan.com/</a></p></td><td><p></p><p></p><p>Mainnet</p></td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Polygon Amoy</p><p><strong>Chain ID</strong>: 80002</p><p><strong>New RPC URL</strong>: https://polygon-amoy.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: MATIC</p><p><strong>Block Explorer</strong>: <a href="https://www.oklink.com/amoy">https://www.oklink.com/amoy</a></p></td><td>Amoy</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Polygon zkEVM Mainnet</p><p><strong>Chain ID</strong>: 1101</p><p><strong>New RPC URL</strong>: https://polygon-zkevm.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://zkevm.polygonscan.com/">https://zkevm.polygonscan.com/</a></p></td><td>zkEVM Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Polygon zkEVM Cardona</p><p><strong>Chain ID</strong>: 2442</p><p><strong>New RPC URL</strong>: https://polygon-zkevm-cardona.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://cardona-zkevm.polygonscan.com">https://cardona-zkevm.polygonscan.com</a></p></td><td>zkEVM<br>Cardona</td></tr></tbody></table>
{% endtab %}

{% tab title="Arbitrum" %}
<table><thead><tr><th width="586.5">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Arbitrum One</p><p><strong>Chain ID</strong>: 42161</p><p><strong>New RPC URL</strong>: https://arbitrum.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://arbiscan.io/">https://arbiscan.io/</a></p></td><td>One</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Arbitrum Nova</p><p><strong>Chain ID</strong>: 42170</p><p><strong>New RPC URL</strong>: https://arbitrum-nova.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://nova.arbiscan.io/">https://nova.arbiscan.io/</a></p></td><td>Nova</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Arbitrum Sepolia</p><p><strong>Chain ID</strong>: 421614</p><p><strong>New RPC URL</strong>: https://arbitrum-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://sepolia-explorer.arbitrum.io">https://sepolia-explorer.arbitrum.io</a></p></td><td>Sepolia</td></tr></tbody></table>
{% endtab %}

{% tab title="OP" %}
<table><thead><tr><th width="559">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI OP Mainnet</p><p><strong>Chain ID</strong>: 10</p><p><strong>New RPC URL</strong>: https://optimism.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://optimistic.etherscan.io/">https://optimistic.etherscan.io/</a></p></td><td>Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI OP Sepolia</p><p><strong>Chain ID</strong>: 11155420</p><p><strong>New RPC URL</strong>: https://optimism-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://optimism-sepolia.blockscout.com/">https://optimism-sepolia.blockscout.com/</a></p></td><td>Sepolia</td></tr></tbody></table>
{% endtab %}

{% tab title="BSC" %}
**Network Name**: BlockPI BSC&#x20;

**Chain ID**: 56

**New RPC URL**: https://bsc.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: BNB

**Block Explorer**: [https://bscscan.com/](https://bscscan.com/)
{% endtab %}

{% tab title="Avalanche" %}
**etwork Name**: BlockPI Avalanche Mainnet

**Chain ID**: 43114

**New RPC URL**: https://avalanche.blockpi.network/v1/rpc/\<your key>

**Currency symbol:** AVAX

**Block Explorer**: [https://snowtrace.io](https://snowtrace.io)
{% endtab %}

{% tab title="zkSync Era" %}
<table><thead><tr><th width="536">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI zkSync Era Mainnet</p><p><strong>Chain ID</strong>: 324</p><p><strong>New RPC URL</strong>: https://zksync-era.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://goerli.explorer.zksync.io">https://goerli.explorer.zksync.io</a></p></td><td>Mainnet</td></tr><tr><td><strong>Network Name</strong>: BlockPI zkSync Era Sepolia<br><strong>Chain ID</strong>: 300<br><strong>New RPC URL</strong>: https://zksync-era-sepolia.blockpi.network/v1/rpc/&#x3C;your key><br><strong>Currency symbo</strong>l: ETH<br><strong>Block Explorer</strong>: <a href="https://sepolia.explorer.zksync.io/">https://sepolia.explorer.zksync.io/</a></td><td>Sepolia</td></tr></tbody></table>


{% endtab %}

{% tab title="Zetachain" %}
<table><thead><tr><th width="538">Specs</th><th>Networks</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Zetachain mainnet</p><p><strong>Chain ID</strong>: 7000</p><p><strong>New RPC URL</strong>: https://zetachain-evm.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ZETA</p><p><strong>Block Explorer</strong>: <a href="https://explorer.zetachain.com/">https://explorer.zetachain.com/</a></p></td><td>Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Zetachain Testnet</p><p><strong>Chain ID</strong>: 7001</p><p><strong>New RPC URL</strong>: https://zetachain-athens-evm.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: aZETA</p><p><strong>Block Explorer</strong>: <a href="https://explorer.zetachain.com/">https://explorer.zetachain.com/</a></p></td><td>Athens</td></tr><tr><td></td><td></td></tr></tbody></table>
{% endtab %}

{% tab title="Starknet" %}
**Network Name**: BlockPI Starknet Mainnet

**Chain ID**: 23448594291968334

**New RPC URL**: https://starknet.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: ETH

**Block Explorer**: [https://starkscan.co](https://starkscan.co)
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Berachain" %}
**Network Name**: BlockPI Berachain Mainnet

**Chain ID**: 80094

**New RPC URL**: https://berachain.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: BERA

**Block Explorer**: [https://berascan.com/](https://berascan.com/)
{% endtab %}

{% tab title="Fantom" %}
**Network Name**: BlockPI Fantom Mainnet

**Chain ID**: 250

**New RPC URL**: https://fantom.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: FTM

**Block Explorer**: [https://ftmscan.com](https://ftmscan.com)
{% endtab %}

{% tab title="Scroll" %}
<table><thead><tr><th width="476.5">Specs</th><th>Networks</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Scroll Mainnet</p><p><strong>Chain ID</strong>: 534352</p><p><strong>New RPC URL</strong>: https://scroll.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://scrollscan.com/">https://scrollscan.com/</a></p></td><td>Scroll Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Scroll Sepolia</p><p><strong>Chain ID</strong>: 534351</p><p><strong>New RPC URL</strong>: https://scroll-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://sepolia-blockscout.scroll.io/">https://sepolia-blockscout.scroll.io/</a></p></td><td>Scroll Sepolia</td></tr></tbody></table>
{% endtab %}

{% tab title="Gnosis" %}
**Network Name**: BlockPI Gnosis Mainnet

**Chain ID**: 100

**New RPC URL**: https://gnosis.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: xDAI

**Block Explorer**: [https://gnosisscan.io/](https://gnosisscan.io/)
{% endtab %}

{% tab title="Cronos" %}
**Network Name**: BlockPI Cronos Mainnet

**Chain ID**: 25

**New RPC URL**: https://cronos.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: CRO

**Block Explorer**: [https://cronoscan.com](https://cronoscan.com)
{% endtab %}

{% tab title="Oasys" %}
**Network Name**: BlockPI Oasys Mainnet

**Chain ID**: 248

**New RPC URL**: https://oasys.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: OAS

**Block Explorer**: [https://scan.oasys.games/](https://scan.oasys.games/)
{% endtab %}

{% tab title="Meter" %}
**Network Name**: BlockPI Meter Mainnet

**Chain ID**: 82

**New RPC URL**: https://meter.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: MTR

**Block Explorer**: [https://scan.meter.io/](https://scan.meter.io/)
{% endtab %}

{% tab title="Base" %}
<table><thead><tr><th width="569">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Base Mainnet</p><p><strong>Chain ID</strong>: 8453</p><p><strong>New RPC URL</strong>: https://base.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://basescan.org/">https://basescan.org/</a> </p></td><td>Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Base Sepolia</p><p><strong>Chain ID</strong>: 84532</p><p><strong>New RPC URL</strong>: https://base-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://base-sepolia.blockscout.com">https://base-sepolia.blockscout.com</a></p></td><td>Sepolia</td></tr></tbody></table>


{% endtab %}

{% tab title="Linea" %}
<table><thead><tr><th width="559">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Linea Mainnet</p><p><strong>Chain ID</strong>: 59144</p><p><strong>New RPC URL</strong>: https://linea.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://lineascan.build">https://lineascan.build</a></p></td><td><p></p><p></p><p>Mainnet</p></td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Linea Sepolia</p><p><strong>Chain ID</strong>: 59141</p><p><strong>New RPC URL</strong>: https://linea-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://goerli.lineascan.build">https://sepolia.lineascan.build</a></p></td><td><p></p><p>Sepolia</p></td></tr></tbody></table>
{% endtab %}

{% tab title="Viction" %}
**Network Name**: BlockPI Viction Mainnet

**Chain ID**: 88

**New RPC URL**: https://viction.blockpi.network/v1/rpc/\<your key>

**Currency symbo**l: VIC

**Block Explorer**: [https://tomoscan.io/](https://tomoscan.io/)
{% endtab %}

{% tab title="Taiko" %}
<table><thead><tr><th width="545">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Taiko Hekla</p><p><strong>Chain ID</strong>: 167009</p><p><strong>New RPC URL</strong>: https://taiko-hekla.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbo</strong>l: ETH</p><p><strong>Block Explorer</strong>: <a href="https://blockscoutapi.hekla.taiko.xyz">https://blockscoutapi.hekla.taiko.xyz</a></p></td><td>Hekla</td></tr></tbody></table>

[](https://tomoscan.io/)
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Merlin" %}
<table><thead><tr><th width="427">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Merlin Mainnet</p><p><strong>Chain ID</strong>: 4200</p><p><strong>New RPC URL</strong>: https://merlin.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: BTC</p><p><strong>Block Explorer</strong>: <a href="https://scan.merlinchain.io">https://scan.merlinchain.io</a></p></td><td>Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Merlin Testnet</p><p><strong>Chain ID</strong>: 686868</p><p><strong>New RPC URL</strong>: https://merlin-testnet.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: BTC</p><p><strong>Block Explorer</strong>: <a href="https://testnet-scan.merlinchain.io">https://testnet-scan.merlinchain.io</a><a href="https://scan.merlinchain.io"></a></p></td><td>Testnet</td></tr></tbody></table>
{% endtab %}

{% tab title="Blast" %}
<table><thead><tr><th width="569">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Blast Mainnet</p><p><strong>Chain ID</strong>: 81457</p><p><strong>New RPC URL</strong>: https://blast.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://blastscan.io/">https://blastscan.io/</a></p></td><td>Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Blast Sepolia</p><p><strong>Chain ID</strong>: 168587773</p><p><strong>New RPC URL</strong>: https://blast-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://testnet.blastscan.io">https://testnet.blastscan.io</a></p></td><td>Sepolia</td></tr></tbody></table>
{% endtab %}

{% tab title="Conflux eSpace" %}
**Network Name**: BlockPI Conflux eSpace&#x20;

**Chain ID**: 1030

**New RPC URL**: https://conflux-espace.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: CFX

**Block Explorer**: evm.confluxscan.net
{% endtab %}

{% tab title="SUI" %}
**Network Name**: BlockPI SUI Mainnet

**Chain ID**: 897796746

**New RPC URL**: https://sui.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: SUI

**Block Explorer**: [https://suiscan.xyz/](https://suiscan.xyz/)
{% endtab %}

{% tab title="Berachain " %}
**Network Name**: BlockPI Berachain Mainnet

**Chain ID**: 80094

**New RPC URL**: https://berachain.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: BERA

**Block Explorer**: [https://berascan.com/](https://berascan.com/)
{% endtab %}

{% tab title="Mantle" %}
**Network Name**: BlockPI Mantle Mainnet

**Chain ID**: 5000

**New RPC URL**: https://mantle.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: MNT

**Block Explorer**: [https://explorer.mantle.xyz](https://explorer.mantle.xyz)
{% endtab %}

{% tab title="Celo" %}
**Network Name**: BlockPI Celo Mainnet

**Chain ID**: 42220

**New RPC URL**: https://celo.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: CELO

**Block Explorer**: [https://celoscan.io\
](https://celoscan.io)
{% endtab %}

{% tab title="Metis" %}
**Network Name**: BlockPI Metis Andromeda Mainnet

**Chain ID**: 1088

**New RPC URL**: https://metis.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: METIS

**Block Explorer**: [https://andromeda-explorer.metis.io](https://andromeda-explorer.metis.io)
{% endtab %}

{% tab title="Unichain" %}
<table><thead><tr><th width="545">Specs</th><th>Network</th></tr></thead><tbody><tr><td><p><strong>Network Name</strong>: BlockPI Unichain Mainnet</p><p><strong>Chain ID</strong>: 130</p><p><strong>New RPC URL</strong>: https://unichain.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://uniscan.xyz">https://uniscan.xyz</a></p></td><td>Mainnet</td></tr><tr><td><p><strong>Network Name</strong>: BlockPI Unichain Sepolia</p><p><strong>Chain ID</strong>: 1301</p><p><strong>New RPC URL</strong>: https://unichain-sepolia.blockpi.network/v1/rpc/&#x3C;your key></p><p><strong>Currency symbol</strong>: ETH</p><p><strong>Block Explorer</strong>: <a href="https://sepolia.uniscan.xyz/">https://sepolia.uniscan.xyz/</a></p></td><td>Sepolia</td></tr></tbody></table>
{% endtab %}

{% tab title="Story" %}
**Network Name**: BlockPI Story Mainnet

**Chain ID**: 1514

**New RPC URL**: https://story.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: IP

**Block Explorer**: [https://mainnet.storyscan.xyz](https://mainnet.storyscan.xyz)
{% endtab %}

{% tab title="Abstract" %}
**Network Name**: BlockPI Abstract Mainnet

**Chain ID**: 2741

**New RPC URL**: https://abstract.blockpi.network/v1/rpc/\<your key>

**Currency symbol**: ETH

**Block Explorer**: [https://abscan.org/](https://abscan.org/)
{% endtab %}
{% endtabs %}
