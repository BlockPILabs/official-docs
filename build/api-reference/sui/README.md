# SUI

BlockPI now supports full-stack data services for SUI, including full nodes, archival services, and GraphQL services. For details on their respective applicable use cases, please refer to the official [documentation](https://docs.sui.io/guides/developer/accessing-data/).&#x20;

<table><thead><tr><th width="142">Stack</th><th width="336">API &#x26; Format</th><th width="151">Data range</th><th>Supported region</th></tr></thead><tbody><tr><td>Mainnet Full node</td><td>JSON-RPC: <br>https://sui.blockpi.network/v1/rpc/&#x3C;key>,<br><br>gRPC: <br>sui.blockpi.network, {token}</td><td>Pruned</td><td>EU, APAC</td></tr><tr><td>Mainnet Archive Service</td><td>gRPC: <br>sui-archive.blockpi.network, {token}</td><td>Archive</td><td>EU, APAC</td></tr><tr><td>Mainnet GraphQL</td><td>GraphQL: <br>https://sui.blockpi.network/v1/graphql/&#x3C;key> </td><td>Latest 90 days</td><td>EU, APAC</td></tr><tr><td>Testnet Full node</td><td>JSON-RPC: <br>https://sui-testnet.blockpi.network/v1/rpc/&#x3C;key>,<br><br>gRPC: <br>sui-testnet.blockpi.network, {token}</td><td>Pruned</td><td>EU, APAC</td></tr></tbody></table>

Since the archival data is within an individual service, the endpoints for the full node (gRPC or deprecated JSON-RPC) and the GraphQL are within "**SUI Mainnet**". While using the archival service, users need to create a separate network endpoint with the name “**SUI Mainnet Archive**”. Check out the above table and the figure below.&#x20;

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Please note that JSON-RPC APIs are only for pruned data and can only be used with a full node endpoint. Users requiring archival data should create a SUI Mainnet Archive endpoint and use gRPC.

{% hint style="info" %}
SUI has announced plans to deprecate the JSON-RPC API. Please refer to the official SUI announcement for the specific timeline. As an official partner, BlockPI will align with SUI’s plan to phase out JSON-RPC support.
{% endhint %}

{% hint style="info" %}
Please see the example in [best-practices.md](../../../basic-tutorials/best-practices.md "mention")to use gRPC in SUI SDK
{% endhint %}
