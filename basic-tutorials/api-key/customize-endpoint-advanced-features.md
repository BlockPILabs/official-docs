---
description: >-
  BlockPI provides users with ample flexibility to customize advanced features
  of their Endpoints, including Archive mode, MEV protection, ERC-4337 Bundler
  service, and more.
icon: galaxy
---

# Customize Endpoint Advanced Features

To determine whether a specific network supports any features, refer to the "Advanced Feature" column in the API Key List. For more detailed supported advanced features, please go to [this page](../../build/supported-networks-and-advanced-features.md).

<figure><img src="../../.gitbook/assets/image (183).png" alt=""><figcaption></figcaption></figure>

## Endpoint Whitelist

Each endpoint can have an independent whitelist, allowing you to set up to 10 IP addresses and domains. Once the whitelist feature is enabled, any requests sent to this endpoint will be checked; if they are not on the whitelist, an error will be returned.

<figure><img src="../../.gitbook/assets/image (182).png" alt=""><figcaption></figcaption></figure>

## Archive Mode

If you require access to data from earlier blocks, you can utilize the **Archive Mode**. This feature enables users to retrieve and access the complete historical data of the blockchain.

Enabling Archive mode will route all requests sent to this API key to the archive nodes of the blockchain network. It's important to note that there is a **30% increase in RU consumption**, since running an archive node requires significant storage capacity.&#x20;

In order to optimize efficiency, we recommend activating Archive mode only when necessary, or generate an individual API key to send the archive requests. Check [best-practices.md](best-practices.md "mention") to more efficiently use the feature. Additionally, processing times may be longer due to the substantial amount of data involved. Check [here ](../../build/supported-networks-and-advanced-features.md)for the full list of chains that the Archive mode is supported.

By default, the Archive mode is set to off. To enable it, simply click on the Archive mode symbol corresponding to the endpoint in the API Key list.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

## ERC-4337 Bundler Service

BlockPI now provides Bundler Service for Account Abstraction users on **OP Mainnet**, **Base Mainnet,** **Polygon Mainnet and Taiko Hekla**. The BlockPI team integrated different open-source Bundler clients in the BlockPI network, providing users with the flexibility to choose their preferred client. The currently supported clients are from Etherspot, Candide, Stackup and Pimlico.

To customize it, go to the BlockPI [dashboard](https://dashboard.blockpi.io), click the endpoint which has the 'ERC-4337' mark. You will be directed to the subpage of the endpoint. (If you do not have any endpoint, please refer to the [Generate API Key](generate-an-api-key.md) page to generate a private endpoint).&#x20;

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

On the subpage of the endpoint, there is the 'AA Service' section, which presents you with five different options to choose.&#x20;

'Auto' is the best practice maintained by the BlockPI team. By selecting 'Auto,' BlockPI will automatically assign the most optimal bundler based on each connectivity condition.

<figure><img src="../../.gitbook/assets/advanced features 1.png" alt=""><figcaption></figcaption></figure>

The remaining four are Bundler clients by Stackup, Candide, Pimlico, and Etherspot. When you choose one of these clients, your requests will be processed exclusively by the selected Bundler client.&#x20;

Please check [this page](../../build/api-reference/polygon/) for Polygon Bundler RPC references.&#x20;

## MEV Protection & Global Cast

To provide users with a better experience in using BlockPI RPC, we have implemented MEV protection function on **BSC Mainnet, Ethereum Mainnet, Base Mainnet, and Polygon Mainnet**. Enabling MEV protection safeguards your transactions against **front-running** and **sandwich attacks**. And this feature does not increase RU consumption. We highly recommend enabling it. We employ the MEV-Boost protocol, which is currently the industry's most mature and stable MEV protection protocols. Additionally, we have implemented our own load balancing mechanism. If there is any congestion on the MEV network, we will immediately route user transaction requests to the public mempool. \
\
In contrast, Global Cast can send users' transactions to BlockPI's global network instead of just sending them to a specific node in the node pool, allowing their transactions to quickly fill the public mempool across the entire blockchain network. With this feature enabled, there are two improvements:

1. **Elimination of Performance Fluctuations**: It removes the performance and network fluctuations of individual RPC nodes, ensuring that users experience the fastest transaction sending from the node pool.
2. **Increased Transaction Success Rate**: It guarantees the success rate of user transactions, ensuring that transactions are effectively and quickly added to the mempool and reach the blockbuilder, especially during times of network congestion like airdrop claim events.

{% hint style="info" %}
This feature is mutually exclusive with the MEV functionality because MEV uses private mempool.
{% endhint %}

To use these functions, go to the Endpoint List of the user's dashboard, click the broadcast icon.

<figure><img src="../../.gitbook/assets/advanced features 2.png" alt=""><figcaption></figcaption></figure>

You are able to switch it to Normal, MEV Protection or Global Cast. Only one of the three can be selected.\


<figure><img src="../../.gitbook/assets/advanced features 3.png" alt=""><figcaption></figcaption></figure>
