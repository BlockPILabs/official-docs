# SUI

BlockPI now supports full-stack data services for SUI, including full nodes, archival services, and indexer services. For details on their respective applicable use cases, please refer to the official [documentation](https://docs.sui.io/guides/developer/accessing-data/).&#x20;

Due to the characteristics of the data architecture, the endpoints for the full node and the indexer are within "SUI Mainnet". While using the archival service, users need to create a separate network endpoint with the name “SUI Mainnet Archive”.<br>

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
Please see the example in [best-practices.md](../../../basic-tutorials/best-practices.md "mention")to use gRPC in SUI SDK
{% endhint %}
