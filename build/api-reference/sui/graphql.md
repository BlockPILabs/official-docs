# GraphQL

### Introduction

While JSON-RPC provides a straightforward method‑based interface, **GraphQL offers greater flexibility and efficiency** by allowing you to request exactly the data you need in a single call. This can significantly reduce bandwidth and improve performance, especially for data‑intensive applications.

For a deep dive into the SUI GraphQL schema and available queries, please refer to the [official SUI GraphQL documentation](https://docs.sui.io/references/sui-graphql).

Use GraphQL RPC with the General-purpose Indexer as a flexible and ergonomic data API to build rich dashboards, explorers, and data-driven apps. The API is powered by an indexer created using the custom indexing framework.

Use GraphQL if your application:

* Requires historical data with configurable retention or filtered access to data, such as all transactions sent by an address.
* Needs to display structured results in a frontend, such as wallets and dashboards.
* Benefits from flexible, composable queries that reduce overfetching.
* Relies on multiple data entities, such as transactions, objects, or events, in a single request, or in a consistent fashion when spread over multiple requests as if the responses came from a snapshot at some checkpoint.

### **BlockPI SUI GraphQL API**

With BlockPI, you can interact with the SUI network using your unique API key through standard GraphQL queries. When users create a key for Sui, it can be used for RPC, gRPC, and GraphQL; the only difference is the endpoint format.&#x20;

The example below demonstrates querying the list of objects owned by a specific SUI address.

```json
// Request
curl --location --request POST 'https://sui.blockpi.network/v1/graphql/<YOUR_API_KEY>' 
--header 'Content-Type: application/json' 
--data-raw '{
    "query": "query {
                    checkpoint1: checkpoint {
                                    networkTotalTransactions
                    }
                    checkpoint2: checkpoint {
                                    networkTotalTransactions
                    }
                    checkpoint3: checkpoint {
                                    networkTotalTransactions
                    }
                    checkpoint4: checkpoint {
                                    networkTotalTransactions
                    }
                    checkpoint5: checkpoint {
                                    networkTotalTransactions
                    }
    }",
    "variables": {}
}'

// Result
{
    "data": {
        "checkpoint1": {
            "networkTotalTransactions": 1234567890
        },
        "checkpoint2": {
            "networkTotalTransactions": 1234567890
        },
        "checkpoint3": {
            "networkTotalTransactions": 1234567890
        },
        "checkpoint4": {
            "networkTotalTransactions": 1234567890
        },
        "checkpoint5": {
            "networkTotalTransactions": 1234567890
        }
    }
}
```

The current  Sui GraphQL  is in beta version. All API elements reference can be found via the  [official SUI GraphQL documentation](https://docs.sui.io/references/sui-graphql).
