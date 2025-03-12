---
icon: cube
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

# Bundler Service

BlockPI now provide Bundler Service for Account Abstraction users on **OP Mainnet**, **Base Mainnet,** **Polygon Mainnet and Taiko Hekla**. We have cooperated with Candide, Stackup, Etherspot and Pimlico and integrated their open-source Bundler clients in BlockPI RPC service network. They are currently run by BlockPI team.&#x20;

We aim to provide users with a seamless and convenient experience while offering highly configurable options. Users are able to send ERC-4337 RPC requests to BlockPI Network with the same RPC endpoint. BlockPI will route these requests to Bundlers deployed by BlockPI team. Users are allow to choose which bundler client to process their request. When users choose the Bundler, they have the option to select a specific client or the **Auto** option. Both approaches involve the participation of the BlockPI Load Balancer, but their logic differs.

<figure><img src="../../.gitbook/assets/bundler 1.png" alt=""><figcaption></figcaption></figure>

When the **Auto** option is selected, the choice of different clients does not impact the load balancing weight determination. The load balancer will select a suitable client server for the user based on the performance and health status of all the client servers.

<figure><img src="../../.gitbook/assets/image (173).png" alt=""><figcaption><p>Bundler Service Workflow (Auto)</p></figcaption></figure>

On the other hand, when a specific client is chosen, let's take Etherspot as an example, the working logic is as follows: the load balancer dynamically selects an available Etherspot Skandha server to process the user's requests in real-time. Other clients serve as backup services and are only utilized when all Etherspot Skandha clients are unavailable. In such cases, the load balancer will reevaluate and choose a backup Bundler client server to handle the requests.

<figure><img src="../../.gitbook/assets/image (175).png" alt=""><figcaption><p>Bundler Service Workflow (Etherspot)</p></figcaption></figure>

Please check the [customization guide](../../basic-tutorials/api-key/customize-endpoint-advanced-features.md) to configure the Bundler service settings.&#x20;
