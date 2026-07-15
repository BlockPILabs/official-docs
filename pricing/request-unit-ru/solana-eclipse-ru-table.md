---
layout:
  width: default
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
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Solana/Eclipse RU table(JSON/gRPC)

<table><thead><tr><th width="421">Request Method</th><th>RU Price</th></tr></thead><tbody><tr><td>Default</td><td>65</td></tr><tr><td>getlargestaccounts</td><td>260</td></tr><tr><td>getsupply</td><td>260</td></tr></tbody></table>

<table><thead><tr><th width="421">gRPC Method</th><th>RU Price</th></tr></thead><tbody><tr><td>/geyser.geyser/getblockheight</td><td>50</td></tr><tr><td>/geyser.geyser/getlatestblockhash</td><td>50</td></tr><tr><td>/geyser.geyser/getslot</td><td>50</td></tr><tr><td>/geyser.geyser/getversion</td><td>50</td></tr><tr><td>/geyser.geyser/isblockhashvalid</td><td>50</td></tr><tr><td>/geyser.geyser/ping</td><td>50</td></tr></tbody></table>

**/geyser.geyser/subscribe** is charged based on the data size. The rate is as default as 5 RUs per 250 byte.

{% hint style="info" %}
When a single method exceeds a certain traffic threshold, we will charge additional RUs based on the excess traffic. The specific method is as follows: when the data volume exceeds 1 MB, it will be calculated by increasing the RU consumption by **100% for every additional 1 MB**.
{% endhint %}
