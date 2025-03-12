---
icon: message-exclamation
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

# RPC Error Reference

When users encounter RPC Errors, they often come from three different domains:

1. **Network errors** - These are unrelated to the RPC service itself, but rather caused by network connectivity issues between the user and the CDN service provider. The error messages are typically traditional network errors, which we will **not** list here.
2. **Errors from the node itself** - We will try to list these as comprehensively as possible to help users troubleshoot.
3. **Service restrictions triggered due to the user's account level** - We will list these in a separate table.

This page is still under continuous improvement. If you encounter an error that is not listed here, please contact us on [Discord ](https://discord.com/invite/xTvGVrGVZv)or open a [support ticket](https://blockpi.io/?contact=ticket).&#x20;

### Node Error Message

<table><thead><tr><th width="293">RPC Error Message</th><th>Causes</th><th>Suggestions</th></tr></thead><tbody><tr><td>404 Client Error: Not Found for url: &#x3C;endpoint></td><td>Beacon chain data pruned. </td><td>Activate Archive Mode for the RPC endpoint</td></tr><tr><td>missing trie node</td><td>Missing historical data</td><td>Activate Archive Mode for the RPC endpoint</td></tr><tr><td>required historical state unavailable</td><td>Missing historical data</td><td>Activate Archive Mode for the RPC endpoint</td></tr><tr><td>missing revert data in call exception</td><td>Missing historical data</td><td>Activate Archive Mode for the RPC endpoint</td></tr></tbody></table>

### BlockPI Error Message

<table><thead><tr><th width="193">RPC Error Message</th><th width="289">Causes</th><th>Suggestions</th></tr></thead><tbody><tr><td>ErrorWsDisabledOnPublicEndpoints</td><td>Websocket is not supported on public endpoints</td><td>Create a private endpoint at https://dashboard.blockpi.io</td></tr><tr><td>ErrorInvalidRequest</td><td>Invalid request</td><td>Double check your request format</td></tr><tr><td>ErrorMaxMessagesExceed</td><td>Batch number exceed the limit</td><td>Decrease the number of payload in one request</td></tr><tr><td>ErrorMaxWsBatchSizeExceed</td><td>Batch number exceed the limit for WSS</td><td>Decrease the number of payload in one request</td></tr><tr><td>ErrorTicketRateLimitExceed</td><td>apikey rate limit exceed</td><td>Decrease the QPS</td></tr><tr><td>ErrorMethodDisabled</td><td>RPC method is disabled</td><td></td></tr><tr><td>ErrorRateLimitExceed</td><td>apikey rate limit exceed</td><td>Decrease the QPS</td></tr><tr><td>ErrMethodLogsArgvLimit1024</td><td>The method is limited to 1024 block range.</td><td>Decrease the number of blocks in one request</td></tr><tr><td>ErrMethodTraceFilterLimit1024</td><td>The method is limited to 1024 block range.</td><td>Decrease the number of blocks in one request</td></tr><tr><td>ErrMethodNewFilterLimit1024</td><td>The method is limited to 1024 block range.</td><td>Decrease the number of blocks in one request</td></tr><tr><td>ErrMethodLogsArgvLimit5000</td><td>The method is limited to 5000 block range with 'address' param.</td><td>Decrease the number of blocks in one request</td></tr><tr><td>ErrMethodNewFilterLimit5000</td><td>The method is limited to 5000 block range with 'address' param.</td><td>Decrease the number of blocks in one request</td></tr><tr><td>ErrMethodTraceFilterLimit5000</td><td>The method is limited to 5000 block range with 'address' param.</td><td>Decrease the number of blocks in one request</td></tr><tr><td>ErrMaxResponseMessageSizeExceed</td><td>max message response size exceed.</td><td>Buy a more advanced RU package</td></tr><tr><td>ErrInvalidTracer</td><td>Invalid tracer. </td><td></td></tr><tr><td>ErrApikeyNotFound</td><td> Apikey not found</td><td>Check the API key status at BlockPI dashboard</td></tr><tr><td>ErrApikeyIsExpired</td><td> Apikey is expired</td><td>Check the API key status at BlockPI dashboard</td></tr><tr><td>ErrUserBalanceIsNotEnough</td><td> Insufficient RU balance</td><td>Buy a RU packag</td></tr></tbody></table>

## Restrictions for Different Endpoint Types

In order to better serve different types of users and ensure the healthy and efficient operation of BlockPI RPC service network, we have implemented different restrictions on various types of endpoints. If a user triggers any of these restrictions, the system will return an error. The following table outlines these limitations:

<table><thead><tr><th>Endpoint Type</th><th width="388.3333333333333">Restrictions </th><th>Error Code</th></tr></thead><tbody><tr><td>Public</td><td>Not support WS/WSS</td><td>N/A</td></tr><tr><td>Public</td><td>Not support Debug_* and Trace_*</td><td>-32000</td></tr><tr><td>Public</td><td>Maximum request rate: 10 qps</td><td>429</td></tr><tr><td>Public</td><td>Maximum response body size: 3 MB</td><td>-32000</td></tr><tr><td>Public</td><td>Maximum block range: 1024</td><td>-32602</td></tr><tr><td>Public</td><td>Maximum batch size: 10</td><td>-32000</td></tr><tr><td>Private</td><td>Maximum block range: 5000 with address input</td><td>-32602</td></tr><tr><td>Private</td><td>Only support “callTracer” and ”prestateTracer” for debug method</td><td>-32000</td></tr><tr><td>Private HTTPS</td><td>Maximum batch size: 1000</td><td>-32000</td></tr><tr><td>Private WSS</td><td>Do not support batch call</td><td>-32000</td></tr><tr><td>All HTTPS</td><td>Do not support subscribe and filter rpc method</td><td>-32000</td></tr></tbody></table>
