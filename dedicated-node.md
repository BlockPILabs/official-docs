---
description: >-
  A dedicated node exclusively occupies a machine, supporting on-demand
  configuration of CPU, memory, and bandwidth.
icon: computer
---

# Dedicated Node

This service is designed for users with high performance and low latency requirements. Users can fully rent a machine, retaining all hardware performance redundancy except for essential monitoring and system software. As a result, there are significant differences in service modes, advantages and disadvantages, and payment models compared to traditional RPC endpoint models. Please read the table below.

|                   | Dedicated Node                | Node Pool                   |
| ----------------- | ----------------------------- | --------------------------- |
| Endpoint          | Configured                    | Domain+key                  |
| Latency           | Ultra-Low                     | Normal                      |
| Rate/method limit | No rate limit or method limit | Has limits                  |
| Node location     | From order                    | Dispatched by load balancer |
| Billing Methods   | By time                       | By RU                       |
| SLA               | Normal                        | Ultra-high                  |

{% hint style="info" %}
The Dedicated Node is an excellent choice for users with high QPS or those sensitive to latency. It offers nearly all advantages, including low per-request costs, low latency, and no limitations on methods.
{% endhint %}

### How to order a Dedicated node

After the users logs in, they can click on the "Dedicated Node" tab in the left sidebar. On the main page, clicking "Add Your First Dedicated Node" will take them to the configuration page.

<figure><img src=".gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

On the configuration page, users need to select the chain, network, node deployment region, client configuration, and payment cycle. It is important to note that subscriptions with a duration of one month will incur a one-time setup fee of $200.

<figure><img src=".gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

After clicking "Apply" in the bottom right corner, a payment interface will pop up displaying the configuration details. Users need to select a payment method to complete the payment.

<figure><img src=".gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

### Dedicated Node List

After ordering, BlockPI will order the machine and deploy the node, which typically takes up to 48 hours to complete. Once there is at least one order, users can view the list of nodes on the Dedicated node page.

<figure><img src=".gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

Users can view the basic information for each node and send RPC requests using the corresponding node URL. It's important to note that even if the node has not expired, users can choose to extend the duration. Clicking the button will pop up the following payment page.

<figure><img src=".gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

If you have customization needs that this configuration page cannot meet, please[contact-us.md](supports/contact-us.md "mention")
