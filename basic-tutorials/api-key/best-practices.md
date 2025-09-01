---
icon: star-christmas
---

# Best Practices

## Success Rate Definition

We present users with a more stringent success rate measurement. Any request that does not receive the expected response is considered unsuccessful in our statistics. This includes, but is not limited to:

1. Any request that triggers BlockPI RPC restrictions, including rate limits, block range limitations, data size limitations, etc.
2. Any error directly returned from the node, such as non-existent methods, incorrect parameters, missing parameters, etc.
3. Others, such as timeout error.

{% hint style="info" %}
We recommend users to output **error logs** so that we can accurately analyze the specific reasons for the unsuccessful requests.
{% endhint %}

## Using Archive Mode

BlockPI Network RPC service allow users to set their endpoint to be with different features, such as Archive mode.&#x20;

When the archive mode is on for a specific endpoint, the requests sent to this endpoint will be routed to archive nodes. And it typically takes a longer time to process due to the huge amount of data.&#x20;

{% hint style="info" %}
In order to more accurately bill users for their requests, we will charge an additional 30% fee for those utilizing archive nodes while keeping the cost for regular requests low.
{% endhint %}

{% hint style="info" %}
As a user, if you wish for your RUs to be utilized efficiently, you may choose to send only those requests which require archive data for processing to the designated endpoint.
{% endhint %}

In this case, you would need to generate two endpoints:

1. one for handling regular requests.
2. another with Archive mode enabled exclusively for processing requests that require archive data. And send requests based on conditions.&#x20;

Here is an example:

{% code overflow="wrap" %}
```python
# Send requests for data that predates 128 blocks to the archive nodes
def request():
    # generate two keys, one is with archive mode enabled
    fullNodeUrl = "https://ethereum.blockpi.network/v1/rpc/<key-normal>"
    archiveNodeUrl = "https://ethereum.blockpi.network/v1/rpc/<key-with-archive-mode-on>"
    
    #target block number
    blockNum = "0x10336aa" 
    
    # get the latest block number
    payload = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 83} 
    headers = {"Content-Type": "application/json"}
    latestNum = requests.post(fullNodeUrl,headers=headers, data=json.dumps(payload)).json()['result']
    
    # Send the request to the desired endpoint.
    traceBlockPayload = {"jsonrpc":"2.0","method":"trace_block","params":[blockNum],"id":1}
    if int(latestNum,16) - int(blockNum,16) >= 128 :
        resp = requests.post(archiveNodeUrl,headers=headers, data=json.dumps(traceBlockPayload))
        print(resp.text)
    else:
        resp = requests.post(fullNodeUrl,headers=headers, data=json.dumps(traceBlockPayload))
        print(resp.text)
```
{% endcode %}

## Segment Block Range in eth\_getLogs

Here is another one with using the eth\_getLogs. As the method consumes decent sever resource.&#x20;

Our limit on eth\_getLogs block range are as follows: if no parameters are included, a single eth\_getLogs request is limited to 1024 blocks. If the request includes either the topic parameter or the address parameter, the limit is set to 5000.

&#x20;If users need to query a block range more than this limit, you can segment it to multiple requests with certain blocks each.

{% code overflow="wrap" %}
```python
import json
import requests

fullNodeUrl = "https://ethereum.blockpi.network/v1/rpc/<your-api-key>"
headers = {"Content-Type": "application/json"}
interval = 1000

def get_logs(from_block_number, to_block_number):
    logs = []
    while from_block_number <= to_block_number:
        end_block_number = min(to_block_number, from_block_number + interval)
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getLogs",
            "params": [{
                "fromBlock": hex(from_block_number),
                "toBlock": hex(end_block_number)
            }]
        }
        response = requests.post(fullNodeUrl, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            raise Exception("Failed to retrieve logs for block range:", from_block_number, end_block_number)
        result = response.json()["result"]
        logs.extend(result)
        from_block_number = end_block_number + 1
        print(response.json())
    return logs

def get_all_logs(from_block_number, to_block_number):
    logs = []
    current_block_number = from_block_number
    while current_block_number <= to_block_number:
        end_block_number = current_block_number + interval
        logs_in_range = get_logs(current_block_number, end_block_number)
        logs.extend(logs_in_range)
        print("Processed block range:", current_block_number, "-", end_block_number, ", total logs:", len(logs_in_range))
        current_block_number = end_block_number + 1
    return logs

from_block_number = 10962850
to_block_number = 10962950

logs = get_all_logs(from_block_number, to_block_number)
print("Total logs:", len(logs))
```
{% endcode %}

## Websocket Reconnection

To safeguard the system, each RPC provider sets a periodic disconnection (timeout) for WebSocket connections. In the case of BlockPI, the timeout is set to 30 minutes. Therefore, during development, users need to implement a mechanism to detect and handle reconnection when the connection is dropped. Here is a Python example:

{% code overflow="wrap" %}
```python
import asyncio
import json
import websockets
​
async def connect(url):
    while True:
        try:
            async with websockets.connect(url) as ws:
                print("websocket connection is established")
                request = {
                    "jsonrpc": "2.0",
                    "id": 2,
                    "method": "eth_subscribe",
                    "params": ["newHeads"]
                }
                await ws.send(json.dumps(request))
​
                while True:
                    message = await ws.recv()
                    print("message received:", message)
​
        except websockets.exceptions.ConnectionClosedError as e:
            if str(e) == 'no close frame received or sent':
                print("keepalive triggered，reconnecting...")
                await asyncio.sleep(5)
                continue
            else:
                print("websocket alive")
                return
        except Exception as e:
            print("Unknown error occurred:", e)
            await asyncio.sleep(5)
            continue
​
if __name__ == "__main__":
    url = "wss://polygon-mumbai.blockpi.network/v1/ws/d69ca19cf64365849ca8152b7f32f319bad9fc22"
    asyncio.run(connect(url))
```
{% endcode %}

{% hint style="warning" %}
Please note that this is just a sample code, and you may need to adapt it to your specific development environment and requirements.
{% endhint %}

## HTTP Batch Call

**What is a Batch Call?**\
A batch call is a JSON-RPC method that bundles multiple requests (like `eth_call` or `eth_getBalance`) into a single HTTP request to an endpoint. This significantly reduces network overhead and latency compared to sending requests individually. Noted that the limit of the batch number is 1000. Any request with more batch calls will be rejected.

**Key Considerations:**

1. **Order:** Responses are returned in the exact same order as the requests.
2. **Independent:** Requests execute separately; one failing doesn't stop the others. You must check each response for errors.
3. **Limits:** Nodes enforce limits on batch size and computational complexity. Exceeding these will cause errors.

## Restrictions for Different Endpoint Types

In order to better serve different types of users and ensure the healthy and efficient operation of BlockPI RPC service network, we have implemented different restrictions on various types of endpoints. If a user triggers any of these restrictions, the system will return an error. The following table outlines these limitations:

<table><thead><tr><th>Endpoint Type</th><th width="388.3333333333333">Restrictions </th><th>Error Code</th></tr></thead><tbody><tr><td>Public</td><td>Not support WS/WSS</td><td>N/A</td></tr><tr><td>Public</td><td>Not support Debug_* and Trace_*</td><td>-32000</td></tr><tr><td>Public</td><td>Maximum request rate: 10 qps</td><td>429</td></tr><tr><td>Public</td><td>Maximum response body size: 3 MB</td><td>-32000</td></tr><tr><td>Public</td><td>Maximum block range: 1024</td><td>-32602</td></tr><tr><td>Public</td><td>Maximum batch size: 10</td><td>-32000</td></tr><tr><td>Private</td><td>Maximum block range: 5000 with address input</td><td>-32602</td></tr><tr><td>Private</td><td>Only support “callTracer” and ”prestateTracer” for debug method</td><td>-32000</td></tr><tr><td>Private HTTPS</td><td>Maximum batch size: 1000</td><td>-32000</td></tr><tr><td>Private WSS</td><td>Do not support batch call</td><td>-32000</td></tr><tr><td>All HTTPS</td><td>Do not support subscribe and filter rpc method</td><td>-32000</td></tr></tbody></table>
