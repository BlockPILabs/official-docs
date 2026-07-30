---
description: >-
  This page serves as a Hyperliquid  API documentation index and lists the
  available methods.
---

# Hyperliquid

BlockPI provides access to HyperLiquid through three distinct endpoint types, each serving a different purpose:

## Endpoint Overview

| Endpoint     | URL                                                            | Protocol    | Use Case                                                                      |
| ------------ | -------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------- |
| **EVM RPC**  | `https://hyperliquid.blockpi.network/v1/rpc/your-api-key`      | JSON-RPC    | Standard Ethereum-compatible blockchain interactions                          |
| **Info**     | `https://hyperliquid.blockpi.network/v1/info/your-api-key`     | REST (POST) | Read-only queries for market data, exchange state, and user information       |
| **Exchange** | `https://hyperliquid.blockpi.network/v1/exchange/your-api-key` | REST (POST) | Trading actions: order placement, cancellation, transfers, account management |
