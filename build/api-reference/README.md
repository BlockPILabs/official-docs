---
description: >-
  This page serves as API documentation index and lists the available JSON-RPC
  methods that BlockPI supports.
icon: rectangle-terminal
---

# API Reference

BlockPI Network is now fully available on more than **60 chains** including Mainnet and Testnet. BlockPI also provide `blockpi_` namespace to provide account information queries.

{% content-ref url="blockpi/" %}
[blockpi](blockpi/)
{% endcontent-ref %}

BlockPI supports WebSocket and HTTPS. Note that the `eth_subscribe` method is only available for WebSocket.&#x20;

To safeguard the RPC node, every RPC provider sets a timeout for WebSocket connections to be disconnected periodically. In the case of BlockPI, the timeout is set to 30 minutes after each connection is established. Please check the code sample of our [best-practices.md](../../basic-tutorials/best-practices.md "mention") page for instruction.

{% hint style="info" %}
If you send batch RPC requests in a single HTTPS request, cost would be based on the number of RPC requests. Note that there is limit time for a Https request. If too many RPC requests are sent with one Https request, there may be a timeout error. So the number is limited to 10 for public endpoints and 1000 for private endpoints.
{% endhint %}
