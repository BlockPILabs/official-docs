---
icon: globe
---

# About BlockPI

{% hint style="info" %}
BlockPI Network Alpha-net officially launched on October 25th, 2022. Compared to Testnet, it is a more stable version and ready for production environments. For more information, please refer to [BlockPI Medium article](https://medium.com/blockpi/blockpi-alpha-net-your-reliable-web3-rpc-service-provider-9574201ec90b).&#x20;
{% endhint %}

BlockPI Network RPC service is supporting more than 60 blockchain networks. Check the full list .

{% content-ref url="../build/supported-networks-and-advanced-features.md" %}
[supported-networks-and-advanced-features.md](../build/supported-networks-and-advanced-features.md)
{% endcontent-ref %}

## Service Structure

BlockPI Network aims to provide high-quality, robust, and efficient RPC service. To avoid the single-point failure and limitation of scalability, the network is designed to be a distributed structure with expandable working nodes. This page introduces the detailed roles and the service mechanisms of the BlockPI Network.

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Users" %}
Users include individual developers, personal users, and blockchain applications. Regardless of the type of user, they send RPC requests through the RPC endpoint domain resolution provided by the RPC provider. Some applications place the RPC endpoint in the web frontend, so users send requests directly from their local machines to the RPC server. Other applications set up backend servers, where users first send requests to the backend of the applications, which then uniformly sends the requests to the RPC provider.
{% endtab %}

{% tab title="Gateway" %}
Gateways collect and sort users' requests, and route them to an appropriate Node Client by the BlockPI Load Balancer. The gateway is divided into general gateways and private gateways. General gateways serve all nodes across all chains, while private gateways are deployed flexibly for customized services.
{% endtab %}

{% tab title="Load Balancer" %}
The load balancer is an algorithm deployed within the Gateway. Our algorithm has undergone multiple iterations, configuring different settings based on the characteristics of each blockchain network to scientifically and reasonably allocate RPC requests to different regions and types of blockchain node clients.
{% endtab %}

{% tab title="Node Client" %}
Node Client is the end node that processes RPC requests and sends responses to users through Gateway. Some blockchain networks have multiple node clients, each with varying performance in handling RPC methods. After thorough testing, we create configurations for specific clients and provide them to the Load Balancer.
{% endtab %}
{% endtabs %}

## Service Lifecycle

* To use the BlockPI Network service, a user must register on [BlockPI Dashboard](https://dashboard.blockpi.io/) and create an API key. At the same time, the RPC endpoint (url) is generated. Different types of RU packages are also available to be purchased by users.
* Requests can be sent by this endpoint and routed to a proper Gateway by DNS.&#x20;
* The Gateway checks the user authority. After that, it sends the request to a Node Client through BlockPI Load Balancer.&#x20;
* Node Client processes the request and produce the response payload. The response is sent back to the Gateway and therefore delivered to the user.

### Guides for users: Jump right in

For a higher quality RPC service, follow these instructions to register and generate your first BlockPI API key.&#x20;

{% content-ref url="../basic-tutorials/registration-and-login/" %}
[registration-and-login](../basic-tutorials/registration-and-login/)
{% endcontent-ref %}

{% content-ref url="../basic-tutorials/api-key/" %}
[api-key](../basic-tutorials/api-key/)
{% endcontent-ref %}

{% content-ref url="../basic-tutorials/wallet-set-up/" %}
[wallet-set-up](../basic-tutorials/wallet-set-up/)
{% endcontent-ref %}

{% content-ref url="../basic-tutorials/account-management/" %}
[account-management](../basic-tutorials/account-management/)
{% endcontent-ref %}

{% content-ref url="../basic-tutorials/team-management/" %}
[team-management](../basic-tutorials/team-management/)
{% endcontent-ref %}
